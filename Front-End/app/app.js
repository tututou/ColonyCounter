/**
 * This is the main module that bootstraps the entire application. All modules containing controllers, services, 
 * or 3rd party libraries must be included in the array below.
 */
angular.module('App', [
  'html-templates',
  'ui.router',
  'ngAnimate', 
  'ngCookies',
  'ngSanitize',
  'ui.router',
  'ngMaterial',
  'nvd3',
  'md.data.table',
  'App.DashboardController',
  'App.NavigationController',
  'App.SidebarController',
  'App.TutorialController',
  'App.ResultController',
  'App.ImageFactory',
  'App.fileInput'
])
.controller('MainController', [ function( ) {
}])
.config(function($stateProvider, $urlRouterProvider, $mdThemingProvider, $httpProvider) {
    
    /**
     *  The routing for the front end application uses ui-router. You can find more information here:
     *  https://github.com/angular-ui/ui-router/wiki
     *
     *  The first state defined here is an "abstract state". 
     *  Read more about abstract states here:
     *  https://github.com/angular-ui/ui-router/wiki/Nested-States-&-Nested-Views#abstract-states
     */
    $stateProvider.state('site', {
            abstract: true,
            views: { 
                'navigation': {
                    templateUrl: 'Controllers/NavigationController/NavigationController.html',
                },
                'content': {
                    templateUrl: 'Controllers/DashboardController/DashboardController.html',
                },
                'sidebar': {
                    templateUrl: 'Controllers/SidebarController/SidebarController.html'
                }
            },
            resolve: {
            }
        })
        .state('site.home', {
            url: '/',
            views: {
                'content@': {
                    templateUrl: 'Controllers/DashboardController/DashboardController.html',
                }
            }
        })
        /**
         * Here we register a route with the URL /tutorial and name site.tutorial
         * We set the attr name in `views` to 'content@' to let the router know that we want this
         * route to exist within the main content area.
         */
        .state('site.tutorial', {
            url: '/tutorial',
            views: {
                'content@': {
                    templateUrl: 'Controllers/TutorialController/TutorialController.html',
                }
            }
        })
        .state('site.result', {
            url: '/result',
            views: {
                'content@': {
                    templateUrl: 'Controllers/ResultController/ResultController.html',
                }
            }
        });
    
    $urlRouterProvider.otherwise('/');

    /**
     * AngularJS Material color schemes can be changed using $mdThemingProvider. 
     * Read more about themes here: https://material.angularjs.org/latest/Theming/03_configuring_a_theme
     */
    $mdThemingProvider.theme('default');
})
.run(function(){

});