angular
    .module('App.ImageFactory', [])
    .factory('ImageFactory', ImageFactory);

ImageFactory.$inject = [
    '$http'
];

function ImageFactory($http){
    var file;    
    var postUrl = 'http://localhost:8000/colonycount/';
    return {
        results: [],
        encodeImage: function(file, onLoadCallback){
            var reader = new FileReader();
            var that = this;
            reader.onload = function(loadEvent) {
                var base64 = loadEvent.target.result.split(',')[1];
                var postBody = {
                    'file' : base64,
                    'type' : '.' + that.getFileExtension(file.name)
                };
                var request = $http.post(postUrl, postBody);
                onLoadCallback(request, base64);
            }
            reader.readAsDataURL(file);
        },
        getFileExtension: function(fileName) {
            var split = fileName.split('.');
            return split[split.length-1];
        }
    }
}