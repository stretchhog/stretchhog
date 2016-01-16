app.controller('TagArchiveCtrl', [
	'$scope', 'EntryService', '$stateParams',
	function ($scope, EntryService, $stateParams) {

		EntryService.getByTag($stateParams.tagSlug).then(function (data) {
			$scope.items = data;
		});

	}]);
