app.factory('EntryService', function ($http) {

	var service = {};

	service.getByYear = function (year) {
		return $http({
			method: 'GET',
			url: '/blog-api/entry/year/' + year
		}).then(function successCallback(response) {
			return response.data;
			// this callback will be called asynchronously
			// when the response is available
		}, function errorCallback(response) {
			// called asynchronously if an error occurs
			// or server returns response with an error status.
		})
	};

	service.getByMonth = function (year, month) {
		return $http({
			method: 'GET',
			url: '/blog-api/entry/month/' + year + '/' + month
		}).then(function successCallback(response) {
			return response.data;
			// this callback will be called asynchronously
			// when the response is available
		}, function errorCallback(response) {
			// called asynchronously if an error occurs
			// or server returns response with an error status.
		})
	};
	service.getBySlug = function (year, month, entrySlug) {
		return $http({
			method: 'GET',
			url: '/blog-api/entry/slug/' + year + '/' + month + '/' + entrySlug
		}).then(function successCallback(response) {
			return response.data;
			// this callback will be called asynchronously
			// when the response is available
		}, function errorCallback(response) {
			// called asynchronously if an error occurs
			// or server returns response with an error status.
		})
	};

	service.getByCategory = function (categorySlug) {
		return $http({
			method: 'GET',
			url: '/blog-api/entry/category/' + categorySlug
		}).then(function successCallback(response) {
			return response.data;
			// this callback will be called asynchronously
			// when the response is available
		}, function errorCallback(response) {
			// called asynchronously if an error occurs
			// or server returns response with an error status.
		})
	};

	service.getAll = function () {
		return $http({
			method: 'GET',
			url: '/blog-api/entry/list'
		}).then(function successCallback(response) {
			return response.data;
			// this callback will be called asynchronously
			// when the response is available
		}, function errorCallback(response) {
			// called asynchronously if an error occurs
			// or server returns response with an error status.
		})
	};

	service.increaseView = function (key) {

	};

	service.increaseLike = function (key) {

	};


	return service
});

