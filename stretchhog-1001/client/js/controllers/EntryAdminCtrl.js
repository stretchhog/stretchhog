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

			$scope.updatePreview = function(item) {
				$http.post('/blog-api/markdown/preview', { preview: item.post }).
				then(function (response) {
					item.preview = response.data.preview;
				});
			};

			// ----------------- COMMENTS --------------------

			$scope.categories = Category.query();
			$scope.tags = Tag.query();
			$scope.resetItem();
		}]);

