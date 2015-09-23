blogApp.factory('tagFactory', function ($resource) {
	return $resource('/blog/admin/tag/:key',
		{
			key: '@key'
		},
		{
			'update': {method: 'PUT'}
		});
})
	.controller('tagController', function tagController($scope, tagFactory, categoryFactory) {

		$scope.tags = [];
		$scope.newTag = {
			tag: '',
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
			$scope.newTag.tag = '';
			$scope.newTag.category = '';
		};

		$scope.toggleEditMode = function (item) {
			// Toggle
			item.editMode = !item.editMode;

			// if item is not in edit mode anymore
			if (!item.editMode) {
				// Restore name
				item.tag = item.serverTag;
				item.category = item.serverCategory;
			} else {
				// save server name to restore it if the user cancel edition
				item.serverTag = item.tag;
				item.serverCategory = item.category;

				// Set edit mode = false and restore the name for the rest of items in edit mode
				// (there should be only one)
				$scope.categories.forEach(function (i) {
					// item is not the item being edited now and it is in edit mode
					if (item.id != i.id && i.editMode) {
						// Restore name
						i.tag = i.serverTag;
						i.category = i.serverCategory;
						i.editMode = false;
					}
				});
			}
		};

		$scope.createItem = function () {
			// Check if the item is already on the list
			tagFactory.save($scope.newTag,
				// success response
				function (createdItem) {
					// Add at the first position
					$scope.tags.unshift(createdItem);
					$scope.newTag.tag = '';
					$scope.newTag.category = '';
				});
		};

		$scope.readItem = function (tagKey) {
			tagFactory.get({key: tagKey});
		};

		$scope.updateItem = function (item) {
			item.editMode = false;

			// Only update if there are changes
			tagFactory.update({key: item.key}, item);
		};

		$scope.deleteItem = function (item) {
			tagFactory.delete({key: item.key}, item, function () {
				// Remove from scope
				var index = $scope.tags.indexOf(item);
				$scope.tags.splice(index, 1);
			});
		};

		$scope.getAllItems = function () {
			$scope.loading = true;
			$scope.tags = tagFactory.query(function () {
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
		$scope.categories = categoryFactory.query()
	});

