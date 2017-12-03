angular.module('keep', []);
angular.module('keep').controller("keepCtrl", function ($scope, $http){


	// $http({ 
	// 	                url: 'http://104.131.166.87:8000/notas/?format=json', 
	// 	                dataType: 'json', 
	// 	                method:'GET',
	// 	                headers: {'Content-Type': 'application/json'}
	// 	            }).then(function (response) {
	// 	                $scope.notas = response;
	// 	            	console.log(response);
	// 	            }).error(function (response) {
	// 	                console.log("deu ruim");           
	// 	            });

	$http.get('http://104.131.166.87:8000/notas/?format=json')
  .then(function (response) {

    var data = response.data;
    $scope.notas = response.data;
    console.log(data);
});


});