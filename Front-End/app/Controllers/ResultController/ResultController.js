angular
    .module('App.ResultController', [])
    .controller('ResultController', ResultController);

ResultController.$inject = [
	'$scope'
];

function ResultController( $scope ) {

	var vm = this;

	init();

	function init() {

	}

}