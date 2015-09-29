blogApp.controller('commentAdminController', [
	'$scope', '$http',
	function ($scope, $http) {

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

