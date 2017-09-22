angular
    .module('App.DashboardController', [])
    .controller('DashboardController', DashboardController);

DashboardController.$inject = [
];

function DashboardController() {

    var vm = this;
    vm.files = [];
    vm.show = show;

    init();

    function init() {

    }

    function show(){
        console.log(vm.files);
    }
}
