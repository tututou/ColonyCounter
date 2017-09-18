var gulp = require('gulp');
var browserSync = require('browser-sync');
var cdnify = require('gulp-cdnizer');
var changed = require('gulp-changed');
var concat = require('gulp-concat');
var css = require('gulp-csso');
var debug = require('gulp-debug');
var del = require('del');
var html2Js = require('gulp-ng-html2js');
var inject = require('gulp-inject');
var maps = require('gulp-sourcemaps');
var merge = require('merge-stream');
var minifyHtml = require('gulp-minify-html');
var ngAnnotate = require('gulp-ng-annotate');
var rename = require('gulp-rename');
var runSequence = require('run-sequence');
var stream = require('streamqueue');
var ugligy = require('gulp-uglify');
var vinylPaths = require('vinyl-paths');
var watch = require('gulp-watch');
var wrap = require('gulp-wrap');

var packageJson = require('./package.json');
var gulpConfig = require('./gulpconfig.js');

gulp.task('style', function() {

    return gulp.src(gulpConfig.appFiles.css)
        .pipe(concat(packageJson.name + '-' + packageJson.version + '.css'))
        .pipe(gulp.dest(gulpConfig.buildDirectory + '/assets/css/'));
});

gulp.task('clean', function() {

    return gulp.src(gulpConfig.buildDirectory)
        .pipe(vinylPaths(del));
});

gulp.task('cleanProd', function() {
    return gulp.src(gulpConfig.prodDirectory)
        .pipe(vinylPaths(del));
});

gulp.task('copy', function() {

    var imgAssets = gulp.src(gulpConfig.appFiles.assets, { base: 'assets/'})
        .pipe(changed(gulpConfig.buildDirectory + 'app/assets'))
        .pipe(gulp.dest(gulpConfig.buildDirectory + 'app/assets'));

    var js = gulp.src(gulpConfig.appFiles.js)
        .pipe(changed(gulpConfig.buildDirectory + '/app'))
        .pipe(wrap('(function(){\n"use strict";\n<%= contents %>}\n)();'))
        .pipe(gulp.dest(gulpConfig.buildDirectory + '/app'));

    var scripts = gulp.src(gulpConfig.appFiles.scripts)
        .pipe(changed(gulpConfig.buildDirectory + '/scripts'))
        .pipe(wrap('(function(){\n"use strict";\n<%= contents %>}\n)();'))
        .pipe(gulp.dest(gulpConfig.buildDirectory + '/scripts'));

    var bowerJS = gulp.src(gulpConfig.bowerLibs.js, {base: '.'})
        .pipe(changed(gulpConfig.buildDirectory))
        .pipe(gulp.dest(gulpConfig.buildDirectory));

    var bowerCSS = gulp.src(gulpConfig.bowerLibs.css, {base: '.'})
        .pipe(changed(gulpConfig.buildDirectory))
        .pipe(gulp.dest(gulpConfig.buildDirectory));

    var fonts = gulp.src(gulpConfig.bowerLibs.fonts, {base: '.'})
        .pipe(changed(gulpConfig.buildDirectory))
        .pipe(gulp.dest(gulpConfig.buildDirectory));

    return merge([imgAssets, js, scripts, bowerJS, bowerCSS, fonts]);
});


// DEPRECATED: Not necessary with current syntax following John Papa's style guide
// https://github.com/johnpapa/angular-styleguide
gulp.task('annotate', function() {
    return gulp.src(gulpConfig.buildDirectory + '/app/**/*.js')
        .pipe(ngAnnotate({ add:true }))
        .pipe(gulp.dest(gulpConfig.buildDirectory + '/app'));
});

gulp.task('ngHtml2Js', function() {
    gulp.src(gulpConfig.appFiles.html)
        .pipe(minifyHtml({
            empty: true,
            spare: true,
            quotes: true
        }))
        .pipe(html2Js({
            moduleName: 'html-templates'
        }))
        .pipe(concat('html-templates.js'))
        .pipe(ugligy())
        .pipe(gulp.dest(gulpConfig.buildDirectory + '/app'));
});

gulp.task('index', function() {
    var index = gulp.src('app/index.html');
    var filesToInject = [].concat(
        gulpConfig.bowerLibs.js,
        gulpConfig.bowerLibs.css,
        gulpConfig.appFiles.scripts,
        gulpConfig.appFiles.js,
        'assets/css/' + packageJson.name + '-' + packageJson.version + '.css',
        'html-templates.js'
    );
    var vinylStreamSource = gulp.src(filesToInject, {
        read: false,
        cwd: gulpConfig.buildDirectory
    });
    return index
        .pipe(inject(vinylStreamSource, { addRootSlash: false }))
        .pipe(gulp.dest(gulpConfig.buildDirectory));
});

gulp.task('watch', function() {
    browserSync({
       port: 1337,
       server: {
           baseDir: gulpConfig.buildDirectory
       }
    });
    gulp.watch([gulpConfig.appFiles.js, gulpConfig.appFiles.scripts, gulpConfig.appFiles.assets],
              function() { runSequence('copy', 'reload') });
    gulp.watch([gulpConfig.appFiles.html],
              function() { runSequence('ngHtml2Js', 'reload') });
    gulp.watch(['index.html'],
              function() { runSequence('index', 'reload') });
    gulp.watch([gulpConfig.appFiles.css],
              function() { runSequence('style', 'reload') });
});

gulp.task('reload', browserSync.reload);

gulp.task('default', function() {
    return runSequence('build', 'watch');
});

gulp.task('build', function() {
    return runSequence('clean', 'style', 'ngHtml2Js', 'copy', 'index');
});
