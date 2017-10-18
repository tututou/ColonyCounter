/**
 * This service acts as a singleton object (google it) that can be shared across many controllers.
 * It's main purpose is to pull files into memory and convert them to base64 to be sent to the server
 * for processing. 
 */
angular
    .module('App.ImageFactory', [])
    .factory('ImageFactory', ImageFactory);

ImageFactory.$inject = [
    '$http'
];

function ImageFactory($http){
    var postUrl = 'http://localhost:8000/colonycount/';
    return {
        /**
         * Array to store results in for display
         */
        results: [],

        /**
         * Takes in a file object containing metadata, and a callback to execute
         * once the file has been uploaded. We pass the POST request object and 
         * the file's base64 to the callback for further handling.
         */ 
        encodeImage: function(file, onLoadCallback){
            /** Read about the FileReader here: 
             * https://stackoverflow.com/questions/36280818/how-to-convert-file-to-base64-in-javascript
             * https://developer.mozilla.org/en-US/docs/Web/API/FileReader
             */
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
        /**
         * Given a filename, returns the file's extension (i.e. 'png')
         */
        getFileExtension: function(fileName) {
            var split = fileName.split('.');
            return split[split.length-1];
        }
    }
}