# New Developers

Welcome to ColonyCounter's front end! Please read through this wiki to get started and learn how the front end application works. 

# Installing Node and NPM

Installing the front end is fairly simple, assuming you have Node.JS installed. If you don't, you can download an installer [here](https://nodejs.org/en/download/). If you're on linux, or use a package manager, read the instructions on how to install node with package managers [here](https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions).

Once you have install Node.JS, you should have access to [node package manager (npm)](https://www.npmjs.com/). To verify, open the command line or terminal, type `npm`, and hit enter. You should see a help dialog. If the `npm` command is not recognized, you need to add it as a PATH variable. You can learn more about doing so [here](https://www.java.com/en/download/help/path.xml).

# Installing the front end

1. From the command line, make sure you have bower installed by running the command `npm install -g bower`
2. With bower installed, navigate to the `Front-End/` directory of the project using the `cd` command. For example, `cd /Users/YourName/ColonyCounter/Front-End/`
3. Before going any further, we need a global installation of GulpJS, which is used as a build tool for the front end. Run the `npm install -g gulp` command.
4. Now that you're inside the `Front-End` directory, we must install the necessary dependencies. Run `npm install && bower install` within this directory.
5. Run `gulp` from within the directory to launch a webserver and view the front end. Congrats, you're all set up!

# A note on GulpJS and the `build/` directory.

Anything that exists within the `Front-End/build/` directory should be considered temporary. When you use GulpJS, it is constantly copying files from the `Front-End/` root and deleting or overwriting what's the `build/` directory, which is where our application is served from. This means that you should be careful to not accidentally start working on any files in this directory, as they'll likely be deleted by GulpJS!

# GulpJS as a build tool

The front end of ColonyCounter uses [GulpJS](https://gulpjs.com/) as a build tool for things like `<script>` tag injection, CSS concatenation, JavaScript minification, serving a webserver, reloading when you update files, and more.

GulpJS is used from the command line by running a command of the `gulp [task name]` format. Below are the tasks you'll find relevant when it comes to development and building the project.

- `gulp` - This is an "all-in-one" command. It cleans the build, re-builds, and then starts a webserver. Leave this running while you're working, it will reload any files that you update into the build directory! If you feel this reload feature isn't working as expected, file an issue.
- `gulp clean` - This deletes the build directory and allows you to start fresh. This is usually chained in other commands as well, but sometimes it feels better on the inside to run this explicitly. 
- `gulp build` - This builds the project without launching a webserver.

# Running things locally

We use GulpJS (as described above) to run the application locally. Simply use the `gulp` command in the `Front-End/` directory after installing the front end to build the application and launch the local webserver.

# Adding a library through bower

If you find a library that you'd like to add to the project, please discuss first with the team. To do so, there are a couple steps you need to take...

1. Within the `Front-End` directory, run `bower install [package-name] --save` to install the package and add its target to the project's `bower.json` file. The `--save` tag is important! If you leave it out you could cause build issues for your teammates, although this isn't the end of the world.
2. Now that you've installed the library, you need to add its relevant files to `Front-End/gulpconfig.js`. This is essentially a JSON object that stores filepaths to relevant files needed by `GulpJS` to build the project. If the file is a JavaScript file, add the main JavaScript file of the library to `bowerLibs.js` in `gulpconfig.js`. If it's a CSS file, add it to `bowerLibs.css`. The specific instructions for the library should inform you which files need to be selected here.
3. Finally, if the library involves some kind of AngularJS module, you need to add it as a dependency in `Front-End/app/app.js`. Add the module name string to the 2nd argument passed to the `angular.module()` method (this is the same array of strings that contains all the controller names. Note you need to do this each time you add a controller as well!).

# AngularJS

The front end of ColonyCounter is built within the framework of [AngularJS](https://angularjs.org/). You can find a tutorial [here](https://docs.angularjs.org/tutorial).

Please note that using AngularJS means that we don't have to use jQuery (and we shouldn't). AngularJS provides [directives](https://docs.angularjs.org/api/ng/directive) that you can tag your HTML elements with in order to add behavior to your views. These directives allow you to do things such as bind HTML element values to JavaScript variables, iterate arrays of objects and render an HTML snippet for each one, show or hide HTML based on a conditional, and more. 

When working on this project, please use the example of how existing features were built to get an idea of how you can approach building your own feature.

# UI Components

For UI components and layout we are using [AngularJS Material](https://material.angularjs.org/latest/). Please make use of these UI components. You should be able to avoid CSS almost entirely using [AngularJS Material's layout system](https://material.angularjs.org/latest/layout/introduction). Please familiarize yourself with how this works. If you are familiar with Bootstrap, this should be easy for you to learn. 


# Creating a new view:

To create a new view given our current workflow, you need to do the following...

1. Add a controller directory to `app/Controllers/` 
2. Create a JavaScript controller file and a corresponding HTML file. Please follow the example and naming convention used by other controllers.
3. Register your new controller within `app.js` as a dependency.
4. Register a new route in `app.js` with `$stateProvider`. [You can read more about how this routing system works here](https://github.com/angular-ui/ui-router/wiki).


```
.state('site.<yourRouteName>', { // 'site.<yourRouteName>' can be referred to in html as ui-sref="site.<yourRouteName>" to create links to your page. 
    url: '/<yourURL>'          // the URL
    views: {
        'content@': {   // 'content@' indicates that this will appear in the main content area
            templateUrl: 'Controllers/<yourControllerDirectory>/<yourControllerHTMLFile>.html', // path to the HTML file
        }
    }
})
```
5. Either navigate to your URL or add a link to it from another view. You can use the `ui-sref` HTML attribute on `<a>` tags to do so, i.e. `<a ui-sref="site.<yourRouteName>">Link to your view</a>`

# Linking your HTML to your JavaScript

Take a look at `Front-End/app/Controllers/DashboardController/DashboardController.html` and `Front-End/app/Controllers/DashboardController/DashboardController.js` to get an idea for how your JavaScript controller can interact with HTML. You need to first scope your html to your controller using `<div ng-controller="MyController as myController"> </div>`. Here, MyController is the AngularJS controller name, and myController is an alias of your choice that is used in HTML to refer to this controller. Any HTML that's then a child of this `<div>` will belong to the scope of the `MyController` JavaScript file, and you can refer to it by its alias.

In `DashboardController.js` you'll see the following line of JavaScript...
```
var vm = this;
```
The name `vm` stands for "view model", and any JavaScript that you want to access in your HTML needs to be added as an attribute to this `vm` object. Have a function that you want to add as a click event on an HTML button? Then the function must be declared as an attribute of the `vm` object. 

You can kind of think of this like you would private and public variables in a language like Java. Any JavaScript variables that exist as attributes of the `vm` object, such as `vm.myFunction` or `vm.myVariable` are public to be used in HTML. Any JavaScript variables or functions that are just declared as a `var` (or really, as long as they're not attributes of `vm`) are private to the controller.

Here's a quick example...

```
// MyController.js
angular
    .module('App.MyController', [])
    .controller('MyController', MyController);

MyController.$inject = [
];

function MyController(){
    var vm = this;
    vm.message = 'Hello world!';
}
```
```
<!-- MyController.html -->
<div ng-controller="MyController as myController">
    <p ng-bind="myController.message">
        <!-- This would set the <p> tag's value to 'Hello world!' -->
    </p>
</div>
```

The `ng-bind` in the above example is just one of the [many components in AngularJS](https://docs.angularjs.org/api/ng/directive). Make use of these to add behavior to your HTML!
