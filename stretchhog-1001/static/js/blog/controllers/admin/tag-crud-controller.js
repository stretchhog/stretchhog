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
			$controller('blog.crud.baseController', {
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

			$scope.updateItem = function (item) {
				item.editMode = false;

				item.category = item.category.key;
				// Only update if there are changes
				tagFactory.update({key: item.key}, item);
			};

			$scope.categories = categoryFactory.query()
		}]);

