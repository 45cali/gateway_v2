angular.module('gatewayApp.services', ['ngResource'])
	.factory('Alerts', function($resource){
		return $resource('/api/get/?format=json');
	});

