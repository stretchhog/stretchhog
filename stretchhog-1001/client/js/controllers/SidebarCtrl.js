app.controller('SidebarCtrl', [
	'$scope', 'SidebarService',
	function ($scope, SidebarService) {

		SidebarService.getCategories().then(function (data) {
			$scope.categories = data;
		});
	}]);

