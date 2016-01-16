app.controller('EntryBannerCtrl', [
	'$scope', 'SlugService', '$stateParams',
	function ($scope, SlugService, $stateParams) {

		SlugService.getEntryForBannerBySlug($stateParams.year, $stateParams.month, $stateParams.entrySlug).then(function (data) {
			$scope.item = data;
		});
	}]);


