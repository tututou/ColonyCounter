angular
    .module('App.TutorialController', [])
    .controller('TutorialController', TutorialController);

TutorialController.$inject = [
	'$scope'
];

function TutorialController( $scope ) {

	var vm = this;

	init();

	function init() {

	}

}