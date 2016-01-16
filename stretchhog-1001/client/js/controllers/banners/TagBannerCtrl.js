app.controller('TagBannerCtrl', [
	'$scope', 'SlugService', '$stateParams',
	function ($scope, SlugService, $stateParams) {

		SlugService.getTagBySlug($stateParams.tagSlug).then(function (data) {
			$scope.item = data;
		});
	}]);


