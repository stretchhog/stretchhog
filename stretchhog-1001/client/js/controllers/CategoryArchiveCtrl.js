app.controller('CategoryArchiveCtrl', [
	'$scope', 'EntryService', '$stateParams',
	function ($scope, EntryService, $stateParams) {

		EntryService.getByCategory($stateParams.categorySlug).then(function (data) {
			$scope.items = data;
		});

	}]);
