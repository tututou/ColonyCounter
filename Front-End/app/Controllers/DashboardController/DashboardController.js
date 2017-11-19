angular
    .module('App.DashboardController', [])
    .controller('DashboardController', DashboardController);

DashboardController.$inject = [
    'ImageFactory',
    '$state'
];

/**
 * Main dashboard controller. Handles image upload form and routing to the
 * results page.
 */
function DashboardController(ImageFactory, $state){
    var vm = this;
    vm.file = [];
    vm.showProgress = false;
    vm.goToThresholding = goToThresholding;
    var validFiletypes = [
        'png',
        'jpg',
        'PNG',
        'JPG'
    ];
    
    init();

    function init() {
        
    }

    function goToThresholding() {
        if (!vm.file || vm.file.length === 0) {
            alert('Please select a file first.');
            return;
        }
        var fileExtension = ImageFactory.getFileExtension(vm.file[0].name);
        if (!arrayContainsAnElement([fileExtension], validFiletypes)) {
            alert('Invalid file type! Must be of type .png or .jpg');
            return;
        }
        ImageFactory.setFile(vm.file[0]);
        vm.showProgress = true;
        ImageFactory.readFromDisk(function() {
            vm.showProgress = false;
            $state.go('site.thresholding');
        });
    }

    // Checks to see if array contains at least one of the elements in searchItems
    function arrayContainsAnElement(array, searchItems) {
        return searchItems.some(elem => array.indexOf(elem) >= 0);
    };
}