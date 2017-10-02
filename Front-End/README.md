# Installing Node and NPM

Installing the front end is fairly simple, assuming you have Node.JS installed. If you don't, you can download an installer [here](www.nodejs.org).

Once you have install Node.JS, you should have access to [node package manager (npm)](https://www.npmjs.com/). To verify, open the command line or terminal, type `npm`, and hit enter. You should see a help dialog. If the `npm` command is not recognized, you need to add it as a PATH variable. You can learn more about doing so [here](https://www.java.com/en/download/help/path.xml).

# Installing the front end

1. From the command line, make sure you have bower installed by running the command `npm install bower`
2. With bower installed, navigate to the `Front-End/` directory of the project using the `cd` command. For example, `cd /Users/YourName/ColonyCounter/Front-End/`
3. Before going any further, we need a global installation of GulpJS, which is used as a build tool for the front end. Run the `npm install -g gulp` command.
4. Now that you're inside the `Front-End` directory, we must install the necessary dependencies. Run `npm install && bower install` within this directory.
5. Run `gulp` from within the directory to launch a webserver and view the front end. Congrats, you're all set up!

# GulpJS as a build tool

The front end of ColonyCounter uses [GulpJS](https://gulpjs.com/) as a build tool for things like `<script>` tag injection, CSS concatenation, JavaScript minification, serving a webserver, reloading when you update files, and more.

GulpJS is used from the command line by running a command of the `gulp [task name]` format. Below are the tasks you'll find relevant when it comes to development and building the project.

- `gulp` - This is an "all-in-one" command. It cleans the build, re-builds, and then starts a webserver. Leave this running while you're working, it will reload any files that you update into the build directory! If you feel this reload feature isn't working as expected, file an issue.
- `gulp clean` - This deletes the build directory and allows you to start fresh. This is usually chained in other commands as well, but sometimes it feels better on the inside to run this explicitly. 
- `gulp build` - This builds the project without launching a webserver.

# Adding a library through bower

If you find a library that you'd like to add to the project, there are a couple steps you need to take...

1. Within the `Front-End` directory, run `bower install [package-name] --save` to install the package and add its target to the project's `bower.json` file. The `--save` tag is important! If you leave it out you could cause build issues for your teammates, although this isn't the end of the world.
2. Now that you've installed the library, you need to add its relevant files to `Front-End/gulpconfig.js`. This is essentially a JSON object that stores filepaths to relevant files needed by `GulpJS` to build the project. If the file is a JavaScript file, add the main JavaScript file of the library to `bowerLibs.js` in `gulpconfig.js`. If it's a CSS file, add it to `bowerLibs.css`. The specific instructions for the library should inform you which files need to be selected here.
3. Finally, if the library involves some kind of AngularJS module, you need to add it as a dependency in `Front-End/app/app.js`. Add the module name string to the 2nd argument passed to the `angular.module()` method (this is the same array of strings that contains all the controller names. Note you need to do this each time you add a controller as well!).

# Setting up Chrome to test
Use these two commands:
1. cd C:\Program Files (x86)\Google\Chrome\Application   
2. chrome.exe --user-data-dir="C:/Chrome dev session" --disable-web-security
