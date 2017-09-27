angular
    .module('App.DashboardController', [])
    .controller('DashboardController', DashboardController);

DashboardController.$inject = [
    'ImageFactory',
    '$scope',
    '$state'
];

function DashboardController(){//$scope, ImageFactory, $state) {

    var vm = this;
    vm.file = [];
    vm.show = show;
    
    init();

    function init() {

    }

    function show(){
        console.log(vm.file);
    }

    function encodeFile(){
        //ImageFactory.encodeImage();
    }
}