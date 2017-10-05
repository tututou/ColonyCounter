angular
    .module('App.ResultController', [])
    .controller('ResultController', ResultController);

ResultController.$inject = [
	'$scope',
	'ImageFactory',
];

function ResultController($scope, ImageFactory){

	var vm = this;
	vm.results = ImageFactory.results;

	init();

	function init() {

	}

}