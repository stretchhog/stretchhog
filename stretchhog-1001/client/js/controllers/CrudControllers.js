app.controller('BaseAdminCtrl', [
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

app.controller('CommentAdminCtrl', [
	'$scope', 'CommentAdminService',
	function ($scope, CommentAdminService) {

		$scope.approveComment = function (comment) {
			comment.approved = true;
			comment.spam = false;
			commentFactory.update({key: comment.key}, comment);
		};

		$scope.spamComment = function (comment) {
			comment.spam = true;
			comment.approved = false;
			commentFactory.update({key: comment.key}, comment);
		};
	}]);

app.controller('EntryAdminCtrl', [
	'$scope', '$controller', '$http', 'Entry', 'Category', 'Tag',
	function ($scope, $controller, $http, Entry, Category, Tag) {
		$controller('BaseAdminCtrl', {
			$scope: $scope,
			factory: Entry
		});

		$scope.filterTags = function (obj) {
			if ($scope.newItem === null) return false;
			return obj.category.key == $scope.newItem.category;
		};

		$scope.resetItem = function () {
			$scope.newItem = {
				title: '',
				summary: '',
				post: '',
				category: '',
				tags: [],
				preview: ''
			}
		};

		$scope.saveToServer = function (item) {
			item.serverTitle = item.title;
			item.serverSummary = item.summary;
			item.serverPost = item.post;
			item.serverTags = item.tags;
			item.serverPreview = item.preview;
		};

		$scope.restoreFromServer = function (item) {
			item.title = item.serverTitle;
			item.summary = item.serverSummary;
			item.post = item.serverPost;
			item.tags = item.serverTags;
			item.preview = item.serverPreview;
		};

		$scope.updatePreview = function (item) {
			$http.post('/blog-api/markdown/preview', {preview: item.post}).then(function (response) {
				item.preview = response.data.preview;
			});
		};

		// ----------------- COMMENTS --------------------

		$scope.categories = Category.query();
		$scope.tags = Tag.query();
		$scope.resetItem();
	}]);

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

