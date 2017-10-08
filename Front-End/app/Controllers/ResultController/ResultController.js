angular
    .module('App.ResultController', [])
    .controller('ResultController', ResultController);

ResultController.$inject = [
	'$scope',
	'ImageFactory',
];

function ResultController($scope, ImageFactory){

	var vm = this;

	init();

	function init() {
		vm.results = ImageFactory.results;
		vm.results.reverse();
	}

}