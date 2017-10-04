angular
    .module('App.DashboardController', [])
    .controller('DashboardController', DashboardController);

DashboardController.$inject = [
    'ImageFactory',
    "$window"
];

function DashboardController(ImageFactory, $window){
    var vm = this;
    vm.file = [];
    vm.showProgress = false;
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
        vm.showProgress = true;
        console.log(vm.file);
        var request = ImageFactory.encodeImage(vm.file[0]);
        request.then(
            function(success){
                vm.showProgress = false;
                console.log("success", success);
            },
            function(error){
                vm.showProgress = false;
                $window.alert("Upload/processing failed, please try resubmitting!");
                console.log("error", error);
            }    
        );
        console.log("yo");
    }

    function clearAll(){
        vm.file = [];
        vm.showProgress = false;
    }
}