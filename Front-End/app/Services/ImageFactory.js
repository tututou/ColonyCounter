angular
    .module('App.ImageFactory', [])
    .factory('ImageFactory', ImageFactory);

ImageFactory.$inject = [
    "$http",
    "$q"
];

function ImageFactory($http){
    var file;    
    return {
        encodeImage: function(file, onLoadCallback){
            var reader = new FileReader();
            reader.onload = function(loadEvent) {
                var base64 = loadEvent.target.result.split(',')[1];
                var postBody = {
                    'file' : base64,
                    'type' : file.type
                };
                var request = $http.post("http://localhost:8000/ccopencv/colonycount/", postBody);
                onLoadCallback(request);
            }
            reader.readAsDataURL(file);
        }
    }
}