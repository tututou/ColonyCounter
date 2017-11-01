angular
.module('App.ThresholdController', [])
.controller('ThresholdController', ThresholdController);

ThresholdController.$inject = [
'ImageFactory',
'$state'
];

/**
* Main dashboard controller. Handles image upload form and routing to the
* results page.
*/
function ThresholdController(ImageFactory, $state){
var vm = this;

init();

function init() {

}

// Uploads the selected image file to memory and sends it in a request
// to the server to apply the CV algorithm to. If a result is received,
// route the application to the results page.
function submitImage() {
    // Check valid file type
    var fileExtension = ImageFactory.getFileExtension(vm.file[0].name);
    if (!arrayContainsAnElement([fileExtension], validFiletypes)) {
        alert('Invalid file type! Must be of type .png or .jpg');
        return;
    }
    vm.showProgress = true;
    // ImageFactory.encodeImage makes a POST request with the image and 
    // receives back a colony count.
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

// Checks to see if array contains at least one of the elements in searchItems
function arrayContainsAnElement(array, searchItems) {
    return searchItems.some(elem => array.indexOf(elem) >= 0);
};
}