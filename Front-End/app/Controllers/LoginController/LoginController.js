angular
    .module('App.LoginController', [])
    .controller('LoginController', LoginController);

NavigationController.$inject = [
	'$mdDialog'
];

function LoginController( $mdDialog ) {

	var vm = this;
	vm.close = close;

	init();

	function close() {
		$mdDialog.hide();
	}

	function init() {

	};
}