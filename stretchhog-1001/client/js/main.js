var app = angular.module('app', ['ngResource', 'ngSanitize', 'ui.router']);

app.config(function ($stateProvider, $urlRouterProvider) {
	$urlRouterProvider.otherwise('/');
	$stateProvider
		.state('home', {
			url: '/',
			templateUrl: '../partials/home.html'
		})
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
			url: '/:year/:month/:entrySlug',
			templateUrl: '../partials/blog/entry/by_slug.html',
			controller: 'EntryCtrl'
		})

		.state('category-archive', {
			url: '/:categorySlug',
			views: {

				// the main template will be placed here (relatively named)
				'': {
					templateUrl: '../partials/blog/archive.html'
				},
				'sidebar@category-archive': {
					templateUrl: '../partials/blog/sidebar.html',
					controller: 'SidebarCtrl'
				},
				'by_category@category-archive': {
					templateUrl: '../partials/blog/category/by_category.html',
					controller: 'CategoryArchiveCtrl'
				}
			}
		})
		.state('month-archive', {
			url: '/:year/:month',
			templateUrl: '../partials/blog/entry/by_month.html',
			controller: 'MonthArchiveCtrl'
		})
		.state('year-archive', {
			url: '/:year',
			templateUrl: '../partials/blog/entry/by_year.html',
			controller: 'YearArchiveCtrl'
		});
});