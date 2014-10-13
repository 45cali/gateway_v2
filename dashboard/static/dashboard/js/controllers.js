var dashCtrl = angular.module('gatewayApp.controllers', []);


dashCtrl.controller('DashboardViewCtrl', function ($scope, $interval, Alerts) {
	$scope.alerts = [];

	Alerts.query(function(response){ $scope.alerts = response});

	$scope.feed = true;

	$interval(function(){
			if ($scope.feed == true){
				Alerts.query(function(response){ 
					$scope.alerts = response;
				})
			}
		  },500
	);

	$scope.toggleFeed = function(){

		$scope.feed = !$scope.feed;

	};



	$scope.predicate = '-id';

    $scope.ticketTypes = {new : true, updated : true, created : true };
	$scope.alertTypes  = {clear : true, info : true, warning : true, critical : true, major : true };
	    
	$scope.modalShown = false;
    $scope.toggleModal = function(alert) {
    	$scope.alertDetail = alert;
    	$scope.modalShown = !$scope.modalShown;	
    };
    $scope.hideModal = function(){
    	$scope.modalShown = false;
    };
    $scope.showModal = function(){
    	$scope.modalShown = true;
    };

});

function NavCtrl($scope, $location){
	$scope.setRoute = function(route){
		$location.path(route);
	}
}