app.factory('entryFactory', function ($resource) {
		return $resource('/blog/admin/entry/:key',
			{
				key: '@key'
			},
			{
				'update': {method: 'PUT'}
			});
	})
	.factory('commentFactory', function ($resource) {
		return $resource('/blog/comment/:key',
			{
				key: '@key'
			},
			{
				'update': {method: 'PUT'}
			});
	})
	.controller('entryController', [
		'$scope', '$controller', '$http', 'entryFactory', 'categoryFactory', 'tagFactory', 'commentFactory',
		function ($scope, $controller, $http, entryFactory, categoryFactory, tagFactory, commentFactory) {
			$controller('blog.CRUD.baseController', {
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
				$http.post('/blog/markdown/preview', { preview: item.post }).
				then(function (response) {
					item.preview = response.data.preview;
				});
			};

			// ----------------- COMMENTS --------------------

			$scope.categories = categoryFactory.query();
			$scope.tags = tagFactory.query();
			$scope.resetItem();
		}]);

