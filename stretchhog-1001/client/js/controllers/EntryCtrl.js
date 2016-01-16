app.controller('EntryCtrl', [
	'$scope', 'SlugService', '$stateParams',
	function ($scope, SlugService, $stateParams) {

		SlugService.getEntryBySlug($stateParams.year, $stateParams.month, $stateParams.entrySlug).then(function (data) {
			$scope.item = data;
		});
	}]);

