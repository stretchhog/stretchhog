angular.module('angularApp', [])
	.controller('categoryFormController', function categoryFormController($scope, $http) {
		$scope.formData = {
			category: null
		};
		$scope.formSubmit = function () {
			$http({
				method: 'POST',
				url: Flask.url_for('create_category'),
				data: $scope.formData
			})
				.then(function (data) {
					$scope.message = data.message;
					$scope.$root.$broadcast('renderCategoryList');
				})
				.catch(function (error) {
					$scope.errorCategory = error.category;
				});
		}
	})
	.controller('categoryListController', function categoryListController($scope, $http) {
		function renderCategoryList() {
			$http({
				method: 'GET',
				url: Flask.url_for('list_category')
			})
				.then(function (response) {
					$scope.categories = response.data;
				})
				.catch(function (error) {
					$scope.errorCategory = error.category;
				});
		}

		$scope.$on('renderCategoryList', renderCategoryList);
		renderCategoryList()
	});