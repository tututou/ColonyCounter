angular
    .module('App.ImageFactory', [])
    .factory('ImageFactory', ImageFactory);

ImageFactory.$inject = [
    '$http'
];

function ImageFactory($http){
    var file;    
    return {
        results: [],
        encodeImage: function(file, onLoadCallback){
            var reader = new FileReader();
            reader.onload = function(loadEvent) {
                var base64 = loadEvent.target.result.split(',')[1];
                var postBody = {
                    'file' : base64,
                    'type' : file.type
                };
                var request = $http.post('http://localhost:8000/ccopencv/colonycount/', postBody);
                onLoadCallback(request, base64);
            }
            reader.readAsDataURL(file);
        }
    }
}