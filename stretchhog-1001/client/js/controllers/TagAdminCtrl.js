app.controller('TagAdminCtrl', [
		'$scope', '$controller', 'Tag', 'Category',
		function ($scope, $controller, Tag, Category) {
			$controller('BaseAdminCtrl', {
				$scope: $scope,
				factory: Tag
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
				Tag.update({key: item.key}, item);
			};

			$scope.categories = Category.query()
		}]);

