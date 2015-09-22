var app = angular.module('angularApp', [])
		.controller('categoryController', function categoryController($scope, $http) {

			function cleanData() {
				$scope.categoryData = {
					category: null
				};
				$scope.edit = false;
			}


			function listCategory() {
				$http({
					method: 'GET',
					url: Flask.url_for('category_cl')
				})
					.then(function (response) {
						$scope.categories = response.data;
					})
					.catch(function (error) {
						$scope.errorCategory = error.category;
					});
			}

			$scope.createCategory = function (isValid) {
				$http({
					method: 'POST',
					url: Flask.url_for('category_cl'),
					data: $scope.categoryData
				})
					.then(function (data) {
						$scope.message = data.message;
						cleanData();
						$scope.$root.$broadcast('listCategory');
					})
					.catch(function (error) {
						$scope.errorCategory = error.category;
					});
			};

			$scope.readCategory = function (categoryKey) {
				$http({
					method: 'GET',
					url: Flask.url_for('category_rud', {key: categoryKey}),
					data: $scope.categoryData
				})
					.then(function (response) {
						$scope.categoryData = response.data;
						$scope.edit = true
					})
					.catch(function (error) {
						$scope.errorCategory = error.category;
					});
			};

			$scope.updateCategory = function (isValid, categoryKey) {
				$http({
						method: 'PUT',
						url: Flask.url_for('category_rud', {key: categoryKey}),
						data: $scope.categoryData
					}
				)
					.then(function (data) {
						$scope.message = data.message;
						cleanData();
						$scope.$root.$broadcast('listCategory');
					})
					.catch(function (error) {
						$scope.errorCategory = error.category;
					});
			};

			$scope.deleteCategory = function (categoryKey) {
				$http({
					method: 'DELETE',
					url: Flask.url_for('category_rud', {key: categoryKey})
				})
					.then(function (data) {
						$scope.message = data.message;
						$scope.$root.$broadcast('listCategory');
					})
					.catch(function (error) {
						$scope.errorCategory = error.category;
					});
			};

			$scope.$on('listCategory', listCategory);
			listCategory();
			$scope.edit = false;

			cleanData();
		})
	;

app.config(['$interpolateProvider', function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{[');
	$interpolateProvider.endSymbol(']}')
}]);