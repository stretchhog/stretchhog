var app = angular.module('app', ['ngResource', 'ngSanitize', 'ui.router']);

app.config(function ($stateProvider, $urlRouterProvider) {

	$stateProvider
		.state('category', {
			url: '/admin/category',
			templateUrl: '../partials/blog/category/categoryCRUD.html',
			controller: 'CategoryCtrl'
		})
});