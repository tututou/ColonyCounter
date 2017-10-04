angular
    .module('App.ImageFactory', [])
    .factory('ImageFactory', ImageFactory);

ImageFactory.$inject = [
    "$http",
    "$q"
];

function ImageFactory($http, $q){    
    return {  

            encodeImage2: function(inputFile) {
                // Upload the file
                // Make the request
                // Take the data from the request return, add it to a $q promise, and then do a deferred.resolve()
                //  which would trigger the "success" of the promis
            },
            file: null,   
            /*uploadFile: function(){
                if (this.file === null || this.file === "" || !this.file){
                    alert("No file has been uploaded");
                    return;
                    }
                   return $http.post("http://localhost:8000/ccopencv/colonycount", {'file' : encodedFile,
                                                                                    'type' : this.file.type});
            },*/
            encodeImage: function(inputFile){
                var reader = new FileReader();
                reader.onload = function(loadEvent){
                    this.file = loadEvent.target.result;
                    if (this.file === null || this.file === "" || !this.file){
                        alert("No file has been uploaded");
                        return;
                        }
                       return $http.post("http://localhost:8000/ccopencv/colonycount", {'file' : encodedFile,
                                                                                        'type' : this.file.type});
                };
                var encodedFile = reader.readAsDataURL(inputFile);
            },
    }
}