angular
    .module('App.ImageFactory', [])
    .factory('ImageFactory', ImageFactory);

ImageFactory.$inject = [
];

function ImageFactory(){
        return {
            encodeImage: $("#file").on('change', function(event){
                    var reader = new FileReader();
                    reader.onload = function(loadEvent){
                        $scope.file = loadEvent.target.result;
                        $scope.$apply();
                    };
                    reader.readAsDataURL(event.target.files[0]);
                }),
                
            uploadFile: function(){
                    if ($scope.file === null || $scope.file === "" || !($scope.file)){
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