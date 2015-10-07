var app = angular.module('app', ['ngResource', 'ngSanitize', 'ui.router']);

app.config(function ($stateProvider, $urlRouterProvider) {

	$stateProvider
		.state('admin-category', {
			url: '/admin/category',
			templateUrl: '../partials/blog/category/categoryCRUD.html',
			controller: 'CategoryAdminCtrl'
		})
		.state('admin-tag', {
			url: '/admin/tag',
			templateUrl: '../partials/blog/tag/tagCRUD.html',
			controller: 'TagAdminCtrl'
		})
		.state('admin-entry', {
			url: '/admin/entry',
			templateUrl: '../partials/blog/entry/entryCRUD.html',
			controller: 'EntryAdminCtrl'
		})

		. state('entry', {
			url: '/:year/:month/:entry-slug',
			templateUrl: '../partials/blog/entry/by_slug.html',
			controller: 'EntryCtrl'
		})
		.state('category-archive', {
			url: '/:categorySlug',
			templateUrl: '../partials/blog/entry/by_category.html',
			controller: 'CategoryArchiveCtrl'
		})
		. state('month-archive', {
			url: '/:year/:month',
			templateUrl: '../partials/blog/entry/by_month.html',
			controller: 'MonthArchiveCtrl'
		})
		. state('year-archive', {
			url: '/:year',
			templateUrl: '../partials/blog/entry/by_year.html',
			controller: 'YearArchiveCtrl'
		})
});