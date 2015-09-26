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
		'$scope', '$controller', 'entryFactory', 'categoryFactory', 'tagFactory',
		function ($scope, $controller, entryFactory, categoryFactory, tagFactory) {
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

			$scope.categories = categoryFactory.query();
			$scope.tags = tagFactory.query();
		}]);

