App.controller('ApplicationCtrl', function ($scope, $location, Restangular, AuthService) {
    $scope.$on('$routeChangeStart', function (event, next) {
        $scope.isLoggedIn = !!AuthService.isAuthenticated();
    });

    $scope.isActive = function(path) {
        if ($location.path().substr(0, path.length) === path) {
            if (path === "/" && $location.path() === "/") {
                return true;
            } else return path !== "/";
        } else {
            return false;
        }
    };
});