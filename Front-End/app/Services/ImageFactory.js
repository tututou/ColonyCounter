angular
    .module('App.ImageFactory', [])
    .factory('ImageFactory', ImageFactory);

ImageFactory.$inject = [
];

function ImageFactory(){
    var file;    
    return {
            encodeImage: function(file){
                var reader = new FileReader();
                reader.onload = function(loadEvent){
                    file = loadEvent.target.result;
                    //uploadFile();
                    console.log(file);
                };
                reader.readAsDataURL(file);
            },
                
            uploadFile: function(){
                    if (file === null || file === "" || !file){
                        alert("No file has been uploaded");
                        return;
                    }
                
                    var dtx = eval("(" + atob($scope.file.substring("data:application/json;base64,".length)) + ")");
                
                    $http.get('yourScript.php?data=' + encodeURIComponent(JSON.stringify(dtx))).then(function(response){
                        if(response.data.status_code == 200){
                            // Done!
                        } else {ERROR}
                    })
        }
    }
}