app.controller('YearArchiveCtrl', [
	'$scope', 'EntryService', '$stateParams',
	function ($scope, EntryService, $stateParams) {

		EntryService.getByYear($stateParams.year).then(function (data) {
			$scope.items = data;
		});
	}]);

