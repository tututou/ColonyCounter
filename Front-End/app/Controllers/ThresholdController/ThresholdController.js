angular
.module('App.ThresholdController', [])
.controller('ThresholdController', ThresholdController);

ThresholdController.$inject = [
'ImageFactory',
'$state'
];

function ThresholdController(ImageFactory, $state){
    var vm = this;
    vm.goToDashboard = goToDashboard;
    vm.threshold = 250;
    vm.updateThreshold = updateThreshold;
    vm.toggleThreshold = toggleThreshold;
    vm.submitImage = submitImage;
    vm.showProgress = false;
    vm.canMakeRequest = true;

    var image;
    var ctx;
    var base64;
    var threshToggled = true;

    init();

    function init() {
        if (!ImageFactory.getBase64()) {
            alert('You must first select an image before thresholding.');
            $state.go('site.home');
        }
        base64 = ImageFactory.getBase64();
        image = new Image();
        var canv = document.createElement("canvas");
        canv.style.width  = '60vh';
        canv.style.height = 'auto';
        document.getElementById('thresh-canvas').appendChild(canv);
        ctx = canv.getContext('2d');
        image.onload = function() {
            updateThreshold();
        };
        image.src = base64;
    }

    function updateThreshold() {
        if (threshToggled) {
            var w = ctx.canvas.width = image.width,
            h = ctx.canvas.height = image.height;
            ctx.drawImage(image, 0, 0, w, h);      
            var d = ctx.getImageData(0, 0, w, h);  
            for (var i=0; i<d.data.length; i+=4) { 
                d.data[i] = d.data[i+1] = d.data[i+2] = d.data[i+1] < vm.threshold ? 0 : 255;
            }
            ctx.putImageData(d, 0, 0);          
        }
    }

    function toggleThreshold() {
        threshToggled = !threshToggled;
        if (threshToggled) {
            updateThreshold();
        } else {
            image.src = base64;
            ctx.drawImage(image, 0, 0, image.width, image.height); 
        }
    }

    function goToDashboard(){
        $state.go('site.home');
    }

    function submitImage() {
        if (vm.canMakeRequest) {
            vm.canMakeRequest = false;
            vm.showProgress = true;
            var threshold = vm.threshold;
            var request = ImageFactory.submitImage(threshold);
            request.then(
                function(success) {     
                    vm.showProgress = false;
                    ImageFactory.results.push({
                        image: ImageFactory.getBase64(),
                        count: success.data.colonyCount,
                        name: ImageFactory.getFile().name,
                        threshold: threshold
                    });
                    vm.canMakeRequest = true;
                    $state.go('site.result');
                },
                function(error) {
                    vm.showProgress = false;
                    vm.canMakeRequest = true;
                    alert("There was an error processing your image, please try submitting it again!");
                });
        }
    }
}