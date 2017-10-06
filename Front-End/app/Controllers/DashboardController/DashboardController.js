angular
    .module('App.DashboardController', [])
    .controller('DashboardController', DashboardController);

DashboardController.$inject = [
    'ImageFactory',
    '$state'
];

function DashboardController(ImageFactory, $state){
    var vm = this;
    vm.file = [];
    vm.showProgress = false;
    vm.submitImage = submitImage;
    vm.clearAll = clearAll;
    var validFiletypes = [
        'png',
        'jpg'
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
                // success.data contains the response data 
                function(success) {     
                    vm.showProgress = false;
                    // We can keep a list of all the results in the ImageFactory for use in the ResultController.
                    // In the ResultController we can ng-repeat over ImageFactory.results to display them.
                    // It's an in-memory array so as long as the user doesn't do a hard refresh of the page, we could 
                    // actually display multiple results if the state of the JavaScript in memory is maintained
                    ImageFactory.results.push({
                        image: img64,
                        count: success.data.colonyCount
                    });
                    console.log(success.data);
                    // Other notes:
                    // use $state.go('site.results'), or whatever the state name is in app.js, to go to the result page.
                    // Read more here: https://github.com/angular-ui/ui-router/wiki/Quick-Reference#stategoto--toparams--options
                },
                function(error) {
                    vm.showProgress = false;
                    // Error stuff. It would be nice to pop up an error message here at the very least. 
                    // for MVP an alert is fine, although in the future we should make some nicer looking messages.
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