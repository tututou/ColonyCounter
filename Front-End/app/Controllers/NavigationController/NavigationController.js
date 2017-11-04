angular
    .module('App.NavigationController', [])
    .controller('NavigationController', NavigationController);

NavigationController.$inject = [
	'$scope',
	'$mdSidenav',
	'$mdDialog'
];

function NavigationController( $scope, $mdSidenav, $mdDialog ) {

	var vm = this;
	vm.openSideNavPanel = openSideNavPanel;
	vm.openLoginPanel = openLoginPanel;

	init();

	function init() {

	}

	function openLoginPanel() {
		$mdDialog.show({
			templateUrl: 'Controllers/LoginController/LoginController.html',
			clickOutsideToClose: true
		})
	}

    function openSideNavPanel() {
        $mdSidenav('left').open();
    };
}