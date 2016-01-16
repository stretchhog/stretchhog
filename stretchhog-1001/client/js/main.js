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

		.state('blog', {
			url: '/blog',
			templateUrl: '../partials/blog/archive.html',
			views: {
				'': {
					templateUrl: '../partials/blog/archive.html'
				},
				'sidebar@blog': {
					templateUrl: '../partials/blog/sidebar.html',
					controller: 'SidebarCtrl'
				},
				'content@blog': {
					templateUrl: '../partials/blog/archive_content.html',
					controller: 'AllArchiveCtrl'
				}
			}
		})

		.state('category-archive', {
			url: '/category/:categorySlug',
			templateUrl: '../partials/blog/archive_content.html',
			views: {
				'': {
					templateUrl: '../partials/blog/archive.html'
				},
				'sidebar@category-archive': {
					templateUrl: '../partials/blog/sidebar.html',
					controller: 'SidebarCtrl'
				},
				'content@category-archive': {
					templateUrl: '../partials/blog/archive_content.html',
					controller: 'CategoryArchiveCtrl'
				}
			}
		})

		.state('entry', {
			url: '/entry/:year/:month/:entrySlug',
			templateUrl: '../partials/blog/archive.html',
			views: {
				'': {
					templateUrl: '../partials/blog/archive.html',
				},
				'sidebar@entry': {
					templateUrl: '../partials/blog/sidebar.html',
					controller: 'SidebarCtrl'
				},
				'content@entry': {
					templateUrl: '../partials/blog/entry/by_slug.html',
					controller: 'EntryCtrl'
				}
			}
		})


		.state('month-archive', {
			url: '/month/:year/:month',
			views: {
				'': {
					templateUrl: '../partials/blog/archive.html'
				},
				'sidebar@month-archive': {
					templateUrl: '../partials/blog/sidebar.html',
					controller: 'SidebarCtrl'
				},
				'content@month-archive': {
					templateUrl: '../partials/blog/archive_content.html',
					controller: 'MonthArchiveCtrl'
				}
			}
		})

		.state('year-archive', {
			url: '/year/:year',
			views: {
				'': {
					templateUrl: '../partials/blog/archive.html'
				},
				'sidebar@year-archive': {
					templateUrl: '../partials/blog/sidebar.html',
					controller: 'SidebarCtrl'
				},
				'content@year-archive': {
					templateUrl: '../partials/blog/archive_content.html',
					controller: 'YearArchiveCtrl'
				}
			}
		})

		.state('tag-archive', {
			url: '/tag/:tagSlug',
			views: {
				'': {
					templateUrl: '../partials/blog/archive.html'
				},
				'sidebar@tag-archive': {
					templateUrl: '../partials/blog/sidebar.html',
					controller: 'SidebarCtrl'
				},
				'content@tag-archive': {
					templateUrl: '../partials/blog/archive_content.html',
					controller: 'TagArchiveCtrl'
				}
			}
		})
});