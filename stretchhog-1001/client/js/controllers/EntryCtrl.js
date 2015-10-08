app.controller('EntryCtrl', [
	'$scope', 'EntryService', '$stateParams',
	function ($scope, EntryService, $stateParams) {

		EntryService.getBySlug($stateParams.year, $stateParams.month, $stateParams.entrySlug).then(function (data) {
			$scope.items = data;
		});
	}]);

