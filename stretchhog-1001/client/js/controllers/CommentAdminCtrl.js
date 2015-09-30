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
