app.controller('blog.public.commentController', [
	'$scope', '$http',
	function ($scope, $http) {

		$scope.initiateComment = function () {
			$scope.comment = {
				parentKey: '',
				name: '',
				email: '',
				comment: '',
				preview: ''
			}
		};

		$scope.initiateMessage = function () {
			$scope.messageGreen = '';
			$scope.messageRed = '';
			$scope.initiateComment();
		};

		$scope.saveComment = function (parentSlug) {
			$scope.comment.parentKey = parentKey;

			$http({
				method: 'GET',
				url: '/comment/'
			}).then(function successCallback(response) {
				// this callback will be called asynchronously
				// when the response is available
			}, function errorCallback(response) {
				// called asynchronously if an error occurs
				// or server returns response with an error status.
			});

			commentFactory.save($scope.comment,
				// success response
				function () {
					// Add at the first position
					$scope.messageGreen = "Thank you for placing a comment. It is placed under review and will be visible once it is approved."
				},
				function () {
					$scope.messageRed = "Something went wrong. Please fill in the form correctly."
				});
		};

		$scope.commentFilter = function (comment) {
			return comment.approved == true;
		};

		$scope.initiateComment();
		$scope.initiateMessage();
	}]);
