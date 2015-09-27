blogApp.factory('entryFactory', function ($resource) {
		return $resource('/blog/admin/entry/:key',
			{
				key: '@key'
			},
			{
				'update': {method: 'PUT'}
			});
	})
	.controller('entryController', [
		'$scope', '$controller', '$http', 'entryFactory', 'categoryFactory', 'tagFactory',
		function ($scope, $controller, $http, entryFactory, categoryFactory, tagFactory) {
			$controller('blog.baseController', {
				$scope: $scope,
				factory: entryFactory
			});

			$scope.filterTags = function (obj) {
				if ($scope.newItem === null) return false;
				return obj.category.key == $scope.newItem.category;
			};

			$scope.filterMusicItems = function (obj) {
				return obj.category.category == 'Music'
			};

			$scope.filterAIItems = function (obj) {
				return obj.category.category == 'Artificial Intelligence'
			};

			$scope.filterFitnessItems = function (obj) {
				return obj.category.category == 'Fitness & Health'
			};

			$scope.resetItem = function resetTag() {
				$scope.newItem = {
					title: '',
					summary: '',
					post: '',
					category: '',
					tags: []
				}
			};

			$scope.saveToServer = function updateTag(item) {
				item.serverTitle = item.title;
				item.serverSummary = item.summary;
				item.serverPost = item.post;
				item.serverTags = item.tags;
			};

			$scope.restoreFromServer = function restoreTag(item) {
				item.title = item.serverTitle;
				item.summary = item.serverSummary;
				item.post = item.serverPost;
				item.tags = item.serverTags;
			};

			$scope.openItem = function (item) {
				item.loadingPost = true;
				if (item.postRendered == null) {
					$http.get('/blog/admin/entry/post/' + item.key).
					then(function (response) {
						item.postRendered = response.data.post;
						item.loadingPost = false;
						item.readMode = true;
					}, function (response) {
						// called asynchronously if an error occurs
						// or server returns response with an error status.
					});
				} else {
					item.readMode = true;
					item.loadingPost = false;
				}
			};

			$scope.closeItem = function (item) {
				item.readMode = false;
			};

			$scope.categories = categoryFactory.query();
			$scope.tags = tagFactory.query();
		}])
;

