angular
    .module('App.ResultController', [])
    .controller('ResultController', ResultController);

ResultController.$inject = [
	'$scope',
	'ImageFactory',
];

function ResultController($scope, ImageFactory){

	var vm = this;
<<<<<<< HEAD
	vm.results = ImageFactory.results;
=======
>>>>>>> refs/remotes/origin/develop

	init();

	function init() {
<<<<<<< HEAD

=======
		vm.results = ImageFactory.results;
		vm.results.reverse();
>>>>>>> refs/remotes/origin/develop
	}

}