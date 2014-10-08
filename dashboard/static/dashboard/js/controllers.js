var dashCtrl = angular.module('gatewayApp.controllers', []);


dashCtrl.controller('DashboardViewCtrl', function ($scope, Alerts) {
	$scope.filters = { };
	$scope.alerts = [];
	Alerts.query(function(response){
		$scope.alerts = response;
	});

});

	
function NavCtrl($scope, $location){
	$scope.setRoute = function(route){
		$location.path(route);
	}
}