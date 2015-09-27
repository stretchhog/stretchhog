blogApp.factory('commentFactory', function ($resource) {
	return $resource('/blog/comment/:key',
		{
			key: '@key'
		},
		{
			'update': {method: 'PUT'}
		});
})
	.controller('tagController', [
		'$scope', '$controller', 'commentFactory',
		function ($scope, $controller, commentFactory) {
			$controller('blog.baseController', {
				$scope: $scope,
				factory: commentFactory
			});

			$scope.resetItem = function resetTag() {
				$scope.newItem.comment = '';
			};

			$scope.saveToServer = function updateTag(item) {
				item.serverComment = item.comment;
			};

			$scope.restoreFromServer = function restoreTag(item) {
				item.comment = item.serverComment;
			};

		}]);

