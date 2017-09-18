/*
 * This file uses node glob patterns (wildcards) to provide the location of all our app
 * files and 3rd party libraries to our gulpfile.js which handles build automation. If you
 * need to add a new bower library be sure to add the file path of all the necessary files 
 * to the appropriate attribute within the bowerLibs objects (i.e. .js go in bowerLibs.js).
 * The build automation ideally should be able to work around modifications to this file alone,
 * so try to avoid editing the gulpfile.js unless necessary (and don't be afraid to ask for 
 * help! :D ) 
 */
module.exports = {
    
    // Dev build is built into ./build/, prod build into ./dist/
    buildDirectory: 'build',
    prodDirectory: 'dist',
    
    /*
     *If we want to use anything other than CSS for styles let me know and I can modify the 
     * gulpfile.js (i.e. if we want to use SASS or LESS).
     */
    appFiles: {
        js: ['app/**/*.js','!app/**/*.spec.js'],
        scripts: ['scripts/*.js', 'services/*.js'],
        html: ['app/**/*.html'],
        css: ['app/**/*.css'],
        assets: ['assets/images/**/*']
    },
    
    bowerLibs: {
        js: [
            'bower_components/angular/angular.js',
            'bower_components/angular-animate/angular-animate.js',
            'bower_components/angular-ui-router/release/angular-ui-router.js',
            'bower_components/angular-aria/angular-aria.js',
            'bower_components/angular-cookies/angular-cookies.js',
            'bower_components/angular-loader/angular-loader.js',
            'bower_components/angular-material/angular-material.js',
            'bower_components/angular-material-data-table/dist/md-data-table.js',
            'bower_components/angular-messages/angular-messages.js',
            'bower_components/angular-mocks/angular-mocks.js',
            'bower_components/angular-nvd3/dist/angular-nvd3.js',
            'bower_components/angular-sanitize/angular-sanitize.js',
            'bower_components/angular-touch/angular-touch.js',
            'bower_components/d3/d3.js',
            'bower_components/nvd3/nv.d3.js',
            'bower_components/jquery/dist/jquery.js',
            'bower_components/oauth-signature/dist/oauth-signature.js'
        ],
        css: [
            'bower_components/angular-material/angular-material.css',
            'bower_components/angular-material-data-table/dist/md-data-table.css',
            'bower_components/nvd3/nv.d3.min.css',
            'bower_components/font-awesome/css/font-awesome.min.css'
        ],
        fonts: [
            'bower_components/font-awesome/fonts/*',
            'bower_components/bootstrap/dist/fonts/*'
        ],
        cdn: [
            {
                file: 'app/bower_components/angular/angular.js',
                package: 'angular',
                cdn: '//ajax.googleapis.com/ajax/libs/angularjs/${version}/angular.min.js'    
            }
        ]
    }
};