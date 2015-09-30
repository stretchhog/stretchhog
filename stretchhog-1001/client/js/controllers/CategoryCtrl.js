app.controller('CategoryCtrl', [
		'$scope', '$controller', 'Category',
		function ($scope, $controller, Category) {
			$controller('blog.crud.baseController', {
				$scope: $scope,
				factory: Category
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

