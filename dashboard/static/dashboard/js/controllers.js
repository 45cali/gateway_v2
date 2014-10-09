var dashCtrl = angular.module('gatewayApp.controllers', []);


dashCtrl.controller('DashboardViewCtrl', function ($scope, Alerts) {
	
	$scope.alerts = [];

	Alerts.query(function(response){
	   $scope.alerts = response;
       
     });

	$scope.predicate = '-id';

    
	$scope.ticketTypes = {new : true, updated : true, created : true };
	$scope.alertTypes  = {clear : true, info : true, warning : true, critical : true, major : true };
    
	
});

	
function NavCtrl($scope, $location){
	$scope.setRoute = function(route){
		$location.path(route);
	}
}