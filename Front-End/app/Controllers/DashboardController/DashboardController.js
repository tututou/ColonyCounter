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
        var request = ImageFactory.encodeImage(vm.file[0]);
        request.then(
            function(success){
                console.log("success", success);
            },
            function(error){
                console.log("error", error);
            }    
        );
        console.log("yo");
    }

    function clearAll(){
        vm.file = [];
    }
}