app.controller('MonthBannerCtrl', [
	'$scope', '$stateParams',
	function ($scope, $stateParams) {
		$scope.month = $stateParams.month
		$scope.year = $stateParams.year
	}]);


