app.controller('CategoryBannerCtrl', [
	'$scope', 'SlugService', '$stateParams',
	function ($scope, SlugService, $stateParams) {

		SlugService.getCategoryBySlug($stateParams.categorySlug).then(function (data) {
			$scope.item = data;
		});
	}]);

app.controller('EntryBannerCtrl', [
	'$scope', 'SlugService', '$stateParams',
	function ($scope, SlugService, $stateParams) {

		SlugService.getEntryForBannerBySlug($stateParams.year, $stateParams.month, $stateParams.entrySlug).then(function (data) {
			$scope.item = data;
		});
	}]);

app.controller('MonthBannerCtrl', [
	'$scope', '$stateParams',
	function ($scope, $stateParams) {
		$scope.month = $stateParams.month
		$scope.year = $stateParams.year
	}]);

app.controller('TagBannerCtrl', [
	'$scope', 'SlugService', '$stateParams',
	function ($scope, SlugService, $stateParams) {

		SlugService.getTagBySlug($stateParams.tagSlug).then(function (data) {
			$scope.item = data;
		});
	}]);

app.controller('YearBannerCtrl', [
	'$scope', '$stateParams',
	function ($scope, $stateParams) {
		$scope.year = $stateParams.year
	}]);
