app.factory('SidebarService', function ($http) {

	var service = {};

	service.getCategories = function () {
		return $http({
			method: 'GET',
			url: '/blog-api/categories'
		}).then(function successCallback(response) {
			return response.data;
			// this callback will be called asynchronously
			// when the response is available
		}, function errorCallback(response) {
			// called asynchronously if an error occurs
			// or server returns response with an error status.
		})
	};

	return service
});
