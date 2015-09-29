blogApp.factory('entryFactory', function ($resource) {
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

				$scope.items.forEach(function (i) {
					if (item.key != i.key && i.readMode) {
						i.readMode = false;
					}
				});
			};

			$scope.closeItem = function (item) {
				item.readMode = false;
			};

			// ----------------- COMMENTS --------------------

			$scope.initiateComment = function () {
				$scope.comment = {
					comment: '',
					parentKey: '',
					email: '',
					name: ''
				}
			};


			$scope.resetMessage = function () {
				$scope.messageGreen = '';
				$scope.messageRed = '';
				$scope.initiateComment();
			};

			$scope.initiateComment();

			$scope.saveComment = function (item) {
				$scope.comment.parentKey = item.key;
				commentFactory.save($scope.comment,
					// success response
					function () {
						// Add at the first position
						$scope.messageGreen = "Thank you for placing a comment. It is placed under review and will be visible once it is approved."
					},
					function () {
						$scope.messageRed = "Something went wrong. Please satisfy the restrictions before placing a comment."
					});
			};

			$scope.commentFilter = function (comment) {
				return comment.approved == true;
			};

			$scope.adminCommentFilter = function (comment) {
				return (comment.spam == false && comment.approved == false)
					|| comment.approved == true;
			};

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

			$scope.comments = [];
			$scope.categories = categoryFactory.query();
			$scope.tags = tagFactory.query();
			$scope.resetMessage();
		}])
;

