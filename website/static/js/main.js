/**
 * Created by tvancann on 08/07/2015.
 */
window.App = angular.module('App', ['ngRoute', 'restangular', 'LocalStorageModule'])

	.run(function($location, Restangular, AuthService) {
		Restangular.setFullRequestInterceptor(function(element, operation, route, url, headers, params, httpConfig) {
			headers['Authorization'] = 'Basic ' + AuthService.getToken();
			return {
				headers: headers
			};
		});

		Restangular.setErrorInterceptor(function(response, deferred, responseHandler) {
			if (response.config.bypassErrorInterceptor) {
				return true;
			} else {
				switch (response.status) {
				case 401:
					AuthService.logout();
					$location.path('/sessions/create');
					break;
				default:
					throw new Error('No handler for status code ' + response.status);
				}
				return false;
			}
		});
	})

	.config(function($routeProvider, RestangularProvider) {

		RestangularProvider.setBaseUrl('http://localhost:8080');

		var partialsDir = '../static/partials';

		var redirectIfAuthenticated = function(route) {
			return function($location, $q, AuthService) {

				var deferred = $q.defer();

				if (AuthService.isAuthenticated()) {
					deferred.reject();
					$location.path(route);
				} else {
					deferred.resolve()
				}

				return deferred.promise;
			}
		};

		var redirectIfNotAuthenticated = function(route) {
			return function($location, $q, AuthService) {

				var deferred = $q.defer();

				if (! AuthService.isAuthenticated()) {
					deferred.reject();
					$location.path(route);
				} else {
					deferred.resolve()
				}

				return deferred.promise;
			}
		};

		$routeProvider
			.when('/', {
				templateUrl: partialsDir + '/home/detail.html'
			})
			.when('/comics', {
				controller: 'ComicsListCtrl',
				templateUrl: partialsDir + '/comics/list.html'
			})
			.when('/sessions/create', {
				controller: 'SessionCreateCtrl',
				templateUrl: partialsDir + '/session/create.html',
				resolve: {
					redirectIfAuthenticated: redirectIfAuthenticated('/posts/create')
				}
			})
			.when('/sessions/destroy', {
				controller: 'SessionDestroyCtrl',
				templateUrl: partialsDir + '/session/destroy.html'
			});
	});
