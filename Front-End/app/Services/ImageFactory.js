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
                // var reader = new FileReader();
                // reader.onload = function(loadEvent){
                //     file = loadEvent.target.result;
                //     //uploadFile();
                //     //console.log(file);
                // };
                // reader.readAsDataURL(file);
               return $http.get("http://localhost:8000/ccopencv/colonycount");
            },
                
            uploadFile: function(){
                    if (file === null || file === "" || !file){
                        alert("No file has been uploaded");
                        return;
                    }
                    
                    $http({
                        method: 'GET',
                        url: '^hello/'
                      }).then(function successCallback(response) {
                          // this callback will be called asynchronously
                          // when the response is available
                        }, function errorCallback(response) {
                          // called asynchronously if an error occurs
                          // or server returns response with an error status.
                        });

                    var dtx = eval("(" + atob($scope.file.substring("data:application/json;base64,".length)) + ")");
                
                    $http.get('yourScript.php?data=' + encodeURIComponent(JSON.stringify(dtx))).then(function(response){
                        if(response.data.status_code == 200){
                            // Done!
                        } else {ERROR}
                    })
        }
    }
}