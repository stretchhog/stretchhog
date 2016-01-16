app.factory('SlugService', function ($http) {

	var service = {};

	service.getEntryBySlug = function (year, month, entrySlug) {
		return $http({
			method: 'GET',
			url: '/blog-api/entry/slug/' + year + '/' + month + '/' + entrySlug
		}).then(function successCallback(response) {
			return response.data;
		}, function errorCallback(response) {
		})
	};

	service.getEntryForBannerBySlug = function (year, month, entrySlug) {
		return $http({
			method: 'GET',
			url: '/blog-api/entry/banner/' + year + '/' + month + '/' + entrySlug
		}).then(function successCallback(response) {
			return response.data;
		}, function errorCallback(response) {
		})
	};

	service.getCategoryBySlug = function (slug) {
		return $http({
			method: 'GET',
			url: '/blog-api/category/slug/' + slug
		}).then(function successCallback(response) {
			return response.data;
		}, function errorCallback(response) {
		})
	};

	service.getTagBySlug = function (slug) {
		return $http({
			method: 'GET',
			url: '/blog-api/tag/slug/' + slug
		}).then(function successCallback(response) {
			return response.data;
		}, function errorCallback(response) {
		})
	};
	return service
});

