blogApp.factory('entryFactory', function ($resource) {
	return $resource('/blog/admin/entry/:key',
		{
			key: '@key'
		},
		{
			'update': {method: 'PUT'}
		});
})
	.controller('entryController', function categoryController($scope, categoryFactory) {

		$scope.categories = [];
		$scope.newCategory = {
			category: ''
		};
		$scope.loading = false;
		$scope.addMode = true;
		$scope.filterText = '';

		$scope.clearFilter = function () {
			$scope.filterText = '';
		};

		$scope.toggleAddMode = function () {
			$scope.addMode = !$scope.addMode;

			// Default new item name is empty
			$scope.newCategory.name = '';
		};

		$scope.toggleEditMode = function (item) {
			// Toggle
			item.editMode = !item.editMode;

			// if item is not in edit mode anymore
			if (!item.editMode) {
				// Restore name
				item.category = item.serverName;
			} else {
				// save server name to restore it if the user cancel edition
				item.serverName = item.category;

				// Set edit mode = false and restore the name for the rest of items in edit mode
				// (there should be only one)
				$scope.categories.forEach(function (i) {
					// item is not the item being edited now and it is in edit mode
					if (item.id != i.id && i.editMode) {
						// Restore name
						i.category = i.serverName;
						i.editMode = false;
					}
				});
			}
		};

		$scope.createItem = function () {
			// Check if the item is already on the list
			categoryFactory.save($scope.newCategory,
				// success response
				function (createdItem) {
					// Add at the first position
					$scope.categories.unshift(createdItem);
					$scope.newCategory.category = '';
				});
		};

		$scope.readItem = function (categoryKey) {
			categoryFactory.get({key: categoryKey});
		};

		$scope.updateItem = function (item) {
			item.editMode = false;

			// Only update if there are changes
			categoryFactory.update({key: item.key}, item);
		};

		$scope.deleteItem = function (item) {
			categoryFactory.delete({key: item.key}, item, function () {
				// Remove from scope
				var index = $scope.categories.indexOf(item);
				$scope.categories.splice(index, 1);
			});
		};

		$scope.getAllItems = function () {
			$scope.loading = true;
			$scope.categories = categoryFactory.query(function () {
				$scope.loading = false;
			});
		};

		$scope.updateOnEnter = function (item, args) {
			// if key is enter
			if (args.keyCode == 13) {
				$scope.updateItem(item);
				// remove focus
				args.target.blur();
			}
		};

		// In add mode, if user press ENTER, add item
		$scope.saveOnEnter = function (args) {
			// if key is enter
			if (args.keyCode == 13) {
				$scope.createItem();
				// remove focus
				args.target.blur();
			}
		};

		$scope.getAllItems();
	});

