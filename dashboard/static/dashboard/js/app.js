var app = angular.module('gatewayApp', [
	   'ngRoute',
       'gatewayApp.controllers',
       'gatewayApp.services',
       'ngResource',	
       'gatewayApp.filters',

		]);

	app.config(function($interpolateProvider, $routeProvider) {

  		$interpolateProvider.startSymbol('[[');
  		$interpolateProvider.endSymbol(']]');

  		$routeProvider.when('/dashboard',{
  			templateUrl: 'static/dashboard/partials/dashboard.html'

  		});


    });

    app.filter


