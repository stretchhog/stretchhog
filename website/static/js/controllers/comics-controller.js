App.controller('ComicsListCtrl', function ($scope, Restangular) {
	$scope.comics = Restangular.all("comics").getList;
});

