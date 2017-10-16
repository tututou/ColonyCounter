angular
    .module('App.DashboardController', [])
    .controller('DashboardController', DashboardController);

DashboardController.$inject = [
    'ImageFactory',
<<<<<<< HEAD
    '$state',
    '$window'
=======
    '$state'
>>>>>>> refs/remotes/origin/develop
];

function DashboardController(ImageFactory, $state, $window){
    var vm = this;
    vm.file = [];
    vm.showProgress = false;
    vm.submitImage = submitImage;
    vm.clearAll = clearAll;
    var validFiletypes = [
        'png',
        'jpg',
        'PNG',
        'JPG'
    ];
    
    init();

    function init() {

    }

    function submitImage() {
        // Check valid file type
        var fileExtension = ImageFactory.getFileExtension(vm.file[0].name);
        if (!arrayContainsAnElement([fileExtension], validFiletypes)) {
            alert('Invalid file type! Must be of type .png or .jpg');
            return;
        }
        vm.showProgress = true;
        ImageFactory.encodeImage(vm.file[0], function(request, img64) {
            request.then(
                function(success) {     
                    vm.showProgress = false;
                    ImageFactory.results.push({
                        image: img64,
                        count: success.data.colonyCount,
                        name: vm.file[0].name
                    });
                    $state.go('site.result');
                },
                function(error) {
                    vm.showProgress = false;
                    alert("There was an error processing your image, please try submitting it again!");
                });
        });
        
    }

    function clearAll(){
        vm.file = [];
        vm.showProgress = false;
    }

    // Checks to see if array contains at least one of the elements in searchItems
    function arrayContainsAnElement(array, searchItems) {
        return searchItems.some(elem => array.indexOf(elem) >= 0);
    };
}