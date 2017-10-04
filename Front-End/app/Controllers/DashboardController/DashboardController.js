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
        ImageFactory.encodeImage(vm.file[0], function(request) {
            request.then(
                function(success) {
                    vm.showProgress = false;
                    // success.data contains the response data
                },
                function(error) {
                    vm.showProgress = false;
                    // error stuff
                });
        });
    }

    function clearAll(){
        vm.file = [];
        vm.showProgress = false;
    }
}