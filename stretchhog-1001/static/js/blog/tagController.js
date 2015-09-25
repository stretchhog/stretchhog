blogApp.factory('tagFactory', function ($resource) {
	return $resource('/blog/admin/tag/:key',
		{
			key: '@key'
		},
		{
			'update': {method: 'PUT'}
		});
})
	.controller('tagController', [
		'$scope', '$controller', 'tagFactory', 'categoryFactory',
		function ($scope, $controller, tagFactory, categoryFactory) {
			$controller('blog.baseController', {
				$scope: $scope,
				factory: tagFactory
			});

			$scope.resetItem = function resetTag() {
				$scope.newItem.tag = '';
				$scope.newItem.category = '';
			};

			$scope.saveToServer = function updateTag(item) {
				item.serverTag = item.tag;
				item.serverCategory = item.category;
			};

			$scope.restoreFromServer = function restoreTag(item) {
				item.tag = item.serverTag;
				item.category = item.serverCategory;
			};

			$scope.categories = categoryFactory.query()
		}]);

