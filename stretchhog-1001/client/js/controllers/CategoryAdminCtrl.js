app.controller('CategoryAdminCtrl', [
		'$scope', '$controller', 'Category',
		function ($scope, $controller, Category) {
			$controller('BaseAdminCtrl', {
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

