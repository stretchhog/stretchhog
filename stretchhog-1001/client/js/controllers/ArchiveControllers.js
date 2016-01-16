app.controller('AllArchiveCtrl', [
	'$scope', 'EntryService',
	function ($scope, EntryService) {

		EntryService.getAll().then(function (data) {
			$scope.items = data;
		});

	}]);


app.controller('CategoryArchiveCtrl', [
	'$scope', 'EntryService', '$stateParams',
	function ($scope, EntryService, $stateParams) {

		EntryService.getByCategory($stateParams.categorySlug).then(function (data) {
			$scope.items = data;
		});

	}]);

app.controller('EntryCtrl', [
	'$scope', 'SlugService', '$stateParams',
	function ($scope, SlugService, $stateParams) {

		SlugService.getEntryBySlug($stateParams.year, $stateParams.month, $stateParams.entrySlug).then(function (data) {
			$scope.item = data;
		});
	}]);

app.controller('MonthArchiveCtrl', [
	'$scope', 'EntryService', '$stateParams',
	function ($scope, EntryService, $stateParams) {

		EntryService.getByMonth($stateParams.year, $stateParams.month).then(function (data) {
			$scope.items = data;
		});
	}]);

app.controller('TagArchiveCtrl', [
	'$scope', 'EntryService', '$stateParams',
	function ($scope, EntryService, $stateParams) {

		EntryService.getByTag($stateParams.tagSlug).then(function (data) {
			$scope.items = data;
		});

	}]);

app.controller('YearArchiveCtrl', [
	'$scope', 'EntryService', '$stateParams',
	function ($scope, EntryService, $stateParams) {

		EntryService.getByYear($stateParams.year).then(function (data) {
			$scope.items = data;
		});
	}]);

app.controller('SidebarCtrl', [
	'$scope', 'SidebarService',
	function ($scope, SidebarService) {

		SidebarService.getCategories().then(function (data) {
			$scope.categories = data;
		});
	}]);

