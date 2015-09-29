blogApp.factory('categoryFactory', function ($resource) {
		return $resource('/blog/admin/category/:key',
			{
				key: '@key'
			},
			{
				'update': {method: 'PUT'}
			});
	})
	.controller('categoryController', [
		'$scope', '$controller', 'categoryFactory',
		function ($scope, $controller, categoryFactory) {
			$controller('blog.crud.baseController', {
				$scope: $scope,
				factory: categoryFactory
			});

			$scope.resetItem = function resetCategory() {
				$scope.newItem.category = '';
			};

			$scope.saveToServer = function updateCategory(item) {
				item.serverCategory = item.category;
			};

			$scope.restoreFromServer = function restoreCategory(item) {
				item.category = item.serverCategory;
			};
		}]);

