angular
    .module('App.ImageFactory', [])
    .factory('ImageFactory', ImageFactory);

ImageFactory.$inject = [
    '$http'
];

function ImageFactory($http){
<<<<<<< HEAD
    var file;    
=======
    var postUrl = 'http://localhost:8000/colonycount/';
>>>>>>> refs/remotes/origin/develop
    return {
        results: [],
        encodeImage: function(file, onLoadCallback){
            var reader = new FileReader();
<<<<<<< HEAD
=======
            var that = this;
>>>>>>> refs/remotes/origin/develop
            reader.onload = function(loadEvent) {
                var base64 = loadEvent.target.result.split(',')[1];
                var postBody = {
                    'file' : base64,
<<<<<<< HEAD
                    'type' : file.type
                };
                var request = $http.post('http://localhost:8000/ccopencv/colonycount/', postBody);
                onLoadCallback(request, base64);
            }
            reader.readAsDataURL(file);
=======
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
>>>>>>> refs/remotes/origin/develop
        }
    }
}