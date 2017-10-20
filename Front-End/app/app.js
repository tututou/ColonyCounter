// Declare app level module which depends on views, and components
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
  '50': 'e4f2fe',
  '100': 'bce0fb',
  '200': '90cbf9',
  '300': '64b6f7',
  '400': '42a6f5',
  '500': '2196f3',
  '600': '1d8ef1',
  '700': '1883ef',
  '800': '1479ed',
  '900': '0b68ea',
  'A100': 'ffffff',
  'A200': 'e1ecff',
  'A400': 'aeccff',
  'A700': '95bcff',
  'contrastDefaultColor': 'light',
  'contrastDarkColors': [
    '50',
    '100',
    '200',
    '300',
    '400',
    'A100',
    'A200',
    'A400',
    'A700'
  ],
  'contrastLightColors': [
    '500',
    '600',
    '700',
    '800',
    '900'
  ]
});

    
  $mdThemingProvider.theme('default')
    .primaryPalette('mcgpalette1')
})
.run(function(){

});