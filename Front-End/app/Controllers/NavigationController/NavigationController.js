angular
    .module('App.NavigationController', [])
    .controller('NavigationController', NavigationController);

NavigationController.$inject = [
	'$scope'
];

function NavigationController( $scope ) {

	var vm = this;

	init();

	function init() {

	}
}