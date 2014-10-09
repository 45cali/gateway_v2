var dashFilters = angular.module('gatewayApp.filters', []);


/*dashFilters.filter('ticketStatusFilter', function(){
	return function(input, filter) {
		var result [];
		anghular.forEach(inpiut, function (ticket){
			angular.forEach(filter, function(isfiltered, type){
				if (isfiltered && type === ticket.type) {
					result.push(ticket);
				}
			});
		});
	  return result;
	};
});






dashFilters.filter('alertStatusFilter', function(){});

/*http://plnkr.co/edit/r1PGIRQI500I8klF5i4I?p=preview*/
/*
<li ng-repeat="(type, value) in winetypes">
      <input type="checkbox" ng-model="winetypes[type]" /> {{type}}
    </li>

    <ul>
      <li ng-repeat="wine in wines | winetypefilter:winetypes">
        {{wine.name}} is a {{wine.type}} with {{wine.style}} style from {{wine.country}}
      </li>

app.filter('winetypefilter', function () {
  return function(input, filter) {
    var result = [];
    angular.forEach(input, function (wine) {
        angular.forEach(filter, function (isfiltered, type) {
            if (isfiltered && type === wine.type) {
                result.push(wine);
            }
        });
    });
    return result;
  };
});

*/