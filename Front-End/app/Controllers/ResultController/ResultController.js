angular
    .module('App.ResultController', [])
    .controller('ResultController', ResultController);

ResultController.$inject = [
	'$scope',
	'ImageFactory'
];
/**
 * Controller used to show colonycount results for images
 */
function ResultController($scope, ImageFactory){

	var vm = this;

	init();

	function init() {
		vm.results = ImageFactory.results.reverse();
	}
}