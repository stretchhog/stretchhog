app.factory('AuthService',
	['$q', '$timeout', '$http',
		function ($q, $timeout, $http) {

			// create user variable
			var user = null;

			// return available functions for use in controllers
			return ({
				isLoggedIn: isLoggedIn,
				login: login,
				logout: logout,
				register: register
			});

			function isLoggedIn() {
				return !!user;
			}

			function login(email, password) {

				// create a new instance of deferred
				var deferred = $q.defer();

				// send a post request to the server
				$http.post('/api/login', {email: email, password: password})
					// handle success
					.success(function (data, status) {
						if (status === 200 && data.result) {
							user = true;
							deferred.resolve();
						} else {
							user = false;
							deferred.reject();
						}
					})
					// handle error
					.error(function (data) {
						user = false;
						deferred.reject();
					});

				// return promise object
				return deferred.promise;

			}

			function logout() {

				// create a new instance of deferred
				var deferred = $q.defer();

				// send a get request to the server
				$http.get('/api/logout')
					// handle success
					.success(function (data) {
						user = false;
						deferred.resolve();
					})
					// handle error
					.error(function (data) {
						user = false;
						deferred.reject();
					});

				// return promise object
				return deferred.promise;

			}

			function register(email, password) {

				// create a new instance of deferred
				var deferred = $q.defer();

				// send a post request to the server
				$http.post('/api/register', {email: email, password: password})
					// handle success
					.success(function (data, status) {
						if (status === 200 && data.result) {
							deferred.resolve();
						} else {
							deferred.reject();
						}
					})
					// handle error
					.error(function (data) {
						deferred.reject();
					});

				// return promise object
				return deferred.promise;
			}
		}
	]
);

