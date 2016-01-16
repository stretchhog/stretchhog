app.controller('AllArchiveCtrl', [
	'$scope', 'EntryService',
	function ($scope, EntryService) {

		EntryService.getAll().then(function (data) {
			$scope.items = data;
		});

	}]);
