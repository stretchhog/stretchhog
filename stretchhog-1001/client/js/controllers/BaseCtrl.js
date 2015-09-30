app.controller('blog.crud.baseController', [
	'$scope', 'factory',
	function ($scope, factory) {
		// override these variables
		$scope.newItem = null;

		// override these functions
		$scope.resetItem = null;
		$scope.saveToServer = null;
		$scope.restoreFromServer = null;

		$scope.items = [];
		$scope.loading = false;
		$scope.addMode = true;
		$scope.filterText = '';

		$scope.clearFilter = function () {
			$scope.filterText = '';
		};

		$scope.toggleAddMode = function () {
			$scope.addMode = !$scope.addMode;

			// Default new item name is empty
			$scope.resetItem()
		};

		$scope.toggleEditMode = function (item) {
			// Toggle
			item.editMode = !item.editMode;

			// if item is not in edit mode anymore
			if (!item.editMode) {
				// Restore name
				$scope.restoreFromServer(item);
			} else {
				// save server name to restore it if the user cancel edition
				$scope.saveToServer(item);

				$scope.items.forEach(function (i) {
					// item is not the item being edited now and it is in edit mode
					if (item.id != i.id && i.editMode) {
						// Restore name
						$scope.restoreFromServer(i);
						i.editMode = false;
					}
				});
			}
		};

		$scope.createItem = function () {
			// Check if the item is already on the list
			factory.save($scope.newItem,
				// success response
				function (createdItem) {
					// Add at the first position
					$scope.items.unshift(createdItem);
					$scope.resetItem();
				});
		};

		$scope.readItem = function (key) {
			factory.get({key: key});
		};

		$scope.updateItem = function (item) {
			item.editMode = false;

			// Only update if there are changes
			factory.update({key: item.key}, item);
		};

		$scope.deleteItem = function (item) {
			factory.delete({key: item.key}, item, function () {
				// Remove from scope
				var index = $scope.items.indexOf(item);
				$scope.items.splice(index, 1);
			});
		};

		$scope.getAllItems = function () {
			$scope.loading = true;
			$scope.items = factory.query(function () {
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
	}]);

