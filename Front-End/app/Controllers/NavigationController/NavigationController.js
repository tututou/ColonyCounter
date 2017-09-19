angular
    .module('App.NavigationController', [])
    .controller('NavigationController', NavigationController);

NavigationController.$inject = [
	'$scope',
	'$mdSidenav'
];

function NavigationController( $scope, $mdSidenav ) {

	var vm = this;
	vm.openSideNavPanel = openSideNavPanel;

	init();

	function init() {

	}

    function openSideNavPanel() {
        $mdSidenav('left').open();
    };
}