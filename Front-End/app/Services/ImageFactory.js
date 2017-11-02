/**
 * This service acts as a singleton object that can be shared across many controllers.
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
    var current64;
    var currentFile;
    return {
        /**
         * Array to store results in for display
         */
        results: [],
        setFile: function(file) {
            currentFile = file;
        },
        getFile: function() {
            return currentFile;
        },
        clearFile: function() {
            currentFile = null;
        },
        getBase64: function() {
            if (!current64) {
                return undefined;      
            }
            return 'data:image/' + this.getCurrentFileExtension() + ';base64,' + current64;
        },
        readFromDisk: function(uploadCallback) {
            var reader = new FileReader();
            // var that = this;
            reader.onload = function(loadEvent) {
                current64 = loadEvent.target.result.split(',')[1];
                uploadCallback();
            }
            reader.readAsDataURL(currentFile);
        },
        submitImage: function(threshold) {
            var data = {
                'file' : current64,
                'type' : '.' + this.getFileExtension(currentFile.name),
                'threshold': threshold
            }
            return $http.post(postUrl, data);
        },
        /**
         * Given a filename, returns the file's extension (i.e. 'png')
         */
        getCurrentFileExtension: function() {
            return this.getFileExtension(currentFile.name);
        },
        getFileExtension: function(fileName) {
            var split = fileName.split('.');
            return split[split.length-1];
        }
    }
}