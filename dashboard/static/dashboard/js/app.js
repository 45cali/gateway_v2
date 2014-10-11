var app = angular.module('gatewayApp', [
	   'ngRoute',
	   'ngResource',
       'gatewayApp.controllers',
       'gatewayApp.services',
       'gatewayApp.directives',
       'gatewayApp.filters',

		]);

	app.config(function($interpolateProvider, $routeProvider) {

  		$interpolateProvider.startSymbol('[[');
  		$interpolateProvider.endSymbol(']]');

  		$routeProvider.when('/dashboard',{
  			templateUrl: 'static/dashboard/partials/dashboard.html'

  		});


    });

	app.run(function($rootScope, $templateCache) {
   		$rootScope.$on('$viewContentLoaded', function() {
      		$templateCache.removeAll();
   		});
	});


