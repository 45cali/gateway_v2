var dashFilters = angular.module('gatewayApp.filters', []);


dashFilters.filter('ticketStatusFilter', function(){
	return function(input, filter) {
		var result = [];
		angular.forEach(input, function (alert){
			angular.forEach(filter, function(isfiltered, ticket_status){
				if (isfiltered && ticket_status === alert.ticket_status) {
					result.push(alert);
				}
			});
		});
	  return result;
	};
});

dashFilters.filter('alertStatusFilter', function(){
	return function(input, filter) {
		var result = [];
		angular.forEach(input, function (alert){
			angular.forEach(filter, function(isfiltered, alert_status){
				if (isfiltered && alert_status === alert.alert_status) {
					result.push(alert);
				}
			});
		});
	  return result;
	};
});






