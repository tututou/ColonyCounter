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
}