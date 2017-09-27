angular
    .module('App.DashboardController', [])
    .controller('DashboardController', DashboardController);

DashboardController.$inject = [
    'ImageFactory'
];

function DashboardController(ImageFactory){
    var vm = this;
    vm.file = [];
    vm.show = show;
    vm.fileChanged = fileChanged;
    vm.clearAll = clearAll;
    
    init();

    function init() {

    }

    function show(){
        console.log(vm.file);
        fileChanged();
    }

    function fileChanged(){
        console.log(vm.file);
        ImageFactory.encodeImage(vm.file[0]);
    }

    function clearAll(){
        vm.file = [];
    }
}