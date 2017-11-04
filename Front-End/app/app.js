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
      'App.LoginController',
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
                templateUrl: 'Controllers/SidebarController/SidebarController.html',
            },
            'login': {
            	templateUrl: 'Controllers/LoginController/LoginController.html'
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
    $mdThemingProvider.definePalette('mcgpalette1', {
        '50': 'fcf3e3',
        '100': 'f9e1ba',
        '200': 'f5cd8c',
        '300': 'f0b85d',
        '400': 'eda93b',
        '900': 'ea9a18',
        '600': 'e79215',
        '700': 'e48811',
        '800': 'e17e0e',
        '500': 'db6c08',
        'A100': '4f1765',
        'A200': '254b15',
        'A400': '537c42',
        'A700': '254b14',
        'contrastDefaultColor': 'light',
        'contrastDarkColors': [
            '50',
            '100',
            '200'
        ],
            'contrastLightColors': [
            '300',
            '400',
            '500',
            '600',
            '700',
            '800',
            '900',
            'A100',
            'A200',
            'A400',
            'A700'
        ]
    });
    $mdThemingProvider.theme('default')
        .primaryPalette('mcgpalette1', {'hue-1': 'A100', 'hue-2': 'A200'});

})
.run(function(){
});