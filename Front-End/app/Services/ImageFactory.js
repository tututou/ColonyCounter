angular
    .module('App.ImageFactory', [])
    .factory('ImageFactory', ImageFactory);

ImageFactory.$inject = [
    "$http"
];

function ImageFactory($http){
    var file;    
    return {
            encodeImage: function(file){
                 var reader = new FileReader();
                 reader.onload = function(loadEvent){
                    file = loadEvent.target.result;
                    uploadFile();
                 };
               var encodedFile = reader.readAsDataURL(file);
               if (file === null || file === "" || !file){
                alert("No file has been uploaded");
                return;
                }
               return $http.post("http://localhost:8000/ccopencv/colonycount", {'file' : encodedFile,
                                                                                'type' : file.type});
            },
                
            uploadFile: function(){
                    var dtx = eval("(" + atob($scope.file.substring("data:application/json;base64,".length)) + ")");
                
                    $http.get('yourScript.php?data=' + encodeURIComponent(JSON.stringify(dtx))).then(function(response){
                        if(response.data.status_code == 200){
                            // Done!
                        } else {ERROR}
                    })
        }
    }
}