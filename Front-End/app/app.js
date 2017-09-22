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
  'App.SidebarController'
])
.controller('MainController', [ function( ) {
}])
.config(function($stateProvider, $urlRouterProvider, $mdThemingProvider) {
    
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
                'content': {
                    templateUrl: 'Controllers/DashboardController/DashboardController.html',
                }
            }
        });
    
    $urlRouterProvider.otherwise('/');

    $mdThemingProvider.theme('default')
      .primaryPalette('red')
      .dark();
})
.run(function(){

});