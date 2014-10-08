angular.module('gatewayApp', [
	   'ngRoute',
       'gatewayApp.controllers',
       'gatewayApp.services',	
       'ngResource',	

		]).config(function($interpolateProvider, $routeProvider) {

  		$interpolateProvider.startSymbol('[[');
  		$interpolateProvider.endSymbol(']]');

  		$routeProvider.when('/dashboard',{
  			templateUrl: 'static/dashboard/partials/dashboard.html'

  		});


});


