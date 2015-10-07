app.controller('MonthArchiveCtrl', [
	'$scope', 'EntryService', '$stateParams',
	function ($scope, EntryService, $stateParams) {

		EntryService.getByMonth($stateParams.year, $stateParams.month).then(function (data) {
			$scope.items = data;
		});
	}]);

