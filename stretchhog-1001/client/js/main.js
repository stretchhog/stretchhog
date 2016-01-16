var app = angular.module('app', ['ngResource', 'ngSanitize', 'ui.router']);

app.config(function ($stateProvider, $urlRouterProvider) {
	$urlRouterProvider.otherwise('/');
	$stateProvider
		.state('home', {
			url: '/',
			templateUrl: '../partials/home.html',
			access: {restricted: false}
		})

		.state('admin-category', {
			url: '/admin/category',
			templateUrl: '../partials/blog/category/categoryCRUD.html',
			controller: 'CategoryAdminCtrl',
			access: {restricted: true}
		})

		.state('admin-tag', {
			url: '/admin/tag',
			templateUrl: '../partials/blog/tag/tagCRUD.html',
			controller: 'TagAdminCtrl',
			access: {restricted: true}
		})

		.state('admin-entry', {
			url: '/admin/entry',
			templateUrl: '../partials/blog/entry/entryCRUD.html',
			controller: 'EntryAdminCtrl',
			access: {restricted: true}
		})

		.state('blog', {
			url: '/blog',
			access: {restricted: false},
			views: {
				'': {
					templateUrl: '../partials/blog/archive.html'
				},
				'sidebar@blog': {
					templateUrl: '../partials/blog/sidebar.html',
					controller: 'SidebarCtrl'
				},
				'blog-content@blog': {
					templateUrl: '../partials/blog/archive_content.html',
					controller: 'AllArchiveCtrl'
				},
				'banner-name@blog': {
					templateUrl: '../partials/blog/banner.name.html',
					controller: function ($scope) {
						$scope.title = 'Blog';
						$scope.subtitle = 'All blog entries';
					}
				},
				'banner-breadcrumbs@blog': {
					templateUrl: '../partials/blog/banner.breadcrumbs.html',
					controller: function ($scope) {
						$scope.breadcrumbs = [
							{name: 'Home', sref: 'home'},
							{name: 'Blog'}
						];
					}
				}
			}
		})

		.state('category-archive', {
			url: '/category/:categorySlug',
			templateUrl: '../partials/blog/archive_content.html',
			access: {restricted: false},
			views: {
				'': {
					templateUrl: '../partials/blog/archive.html'
				},
				'sidebar@category-archive': {
					templateUrl: '../partials/blog/sidebar.html',
					controller: 'SidebarCtrl'
				},
				'blog-content@category-archive': {
					templateUrl: '../partials/blog/archive_content.html',
					controller: 'CategoryArchiveCtrl'
				},
				'banner-name@category-archive': {
					templateUrl: '../partials/blog/banners/category.html',
					controller: 'CategoryBannerCtrl'
				},
				'banner-breadcrumbs@category-archive': {
					templateUrl: '../partials/blog/breadcrumbs/category.html',
					controller: 'CategoryBannerCtrl'
				}
			}
		})

		.state('entry', {
			url: '/entry/:year/:month/:entrySlug',
			templateUrl: '../partials/blog/archive.html',
			access: {restricted: false},
			views: {
				'': {
					templateUrl: '../partials/blog/archive.html',
				},
				'sidebar@entry': {
					templateUrl: '../partials/blog/sidebar.html',
					controller: 'SidebarCtrl'
				},
				'blog-content@entry': {
					templateUrl: '../partials/blog/entry/by_slug.html',
					controller: 'EntryCtrl'
				},
				'banner-name@entry': {
					templateUrl: '../partials/blog/banners/entry.html',
					controller: 'EntryBannerCtrl'
				},
				'banner-breadcrumbs@entry': {
					templateUrl: '../partials/blog/breadcrumbs/entry.html',
					controller: 'EntryBannerCtrl'
				}
			}
		})

		.state('month-archive', {
			url: '/month/:year/:month',
			access: {restricted: false},
			views: {
				'': {
					templateUrl: '../partials/blog/archive.html'
				},
				'sidebar@month-archive': {
					templateUrl: '../partials/blog/sidebar.html',
					controller: 'SidebarCtrl'
				},
				'blog-content@month-archive': {
					templateUrl: '../partials/blog/archive_content.html',
					controller: 'MonthArchiveCtrl'
				},
				'banner-name@month-archive': {
					templateUrl: '../partials/blog/banners/month.html',
					controller: 'MonthBannerCtrl'
				},
				'banner-breadcrumbs@month-archive': {
					templateUrl: '../partials/blog/breadcrumbs/month.html',
					controller: 'MonthBannerCtrl'
				}
			}
		})

		.state('year-archive', {
			url: '/year/:year',
			access: {restricted: false},
			views: {
				'': {
					templateUrl: '../partials/blog/archive.html'
				},
				'sidebar@year-archive': {
					templateUrl: '../partials/blog/sidebar.html',
					controller: 'SidebarCtrl'
				},
				'blog-content@year-archive': {
					templateUrl: '../partials/blog/archive_content.html',
					controller: 'YearArchiveCtrl'
				},
				'banner-name@year-archive': {
					templateUrl: '../partials/blog/banners/year.html',
					controller: 'YearBannerCtrl'
				},
				'banner-breadcrumbs@year-archive': {
					templateUrl: '../partials/blog/breadcrumbs/year.html',
					controller: 'YearBannerCtrl'
				}
			}
		})

		.state('tag-archive', {
			url: '/tag/:tagSlug',
			access: {restricted: false},
			views: {
				'': {
					templateUrl: '../partials/blog/archive.html'
				},
				'sidebar@tag-archive': {
					templateUrl: '../partials/blog/sidebar.html',
					controller: 'SidebarCtrl'
				},
				'blog-content@tag-archive': {
					templateUrl: '../partials/blog/archive_content.html',
					controller: 'TagArchiveCtrl'
				},
				'banner-name@tag-archive': {
					templateUrl: '../partials/blog/banners/tag.html',
					controller: 'TagBannerCtrl'
				},
				'banner-breadcrumbs@tag-archive': {
					templateUrl: '../partials/blog/breadcrumbs/tag.html',
					controller: 'TagBannerCtrl'
				}


			}
		})

		.state('login', {
			"url": '/login',
			access: {restricted: false},
			views: {
				'': {
					templateUrl: '../partials/login.html',
					controller: 'LoginCtrl'
				},
				'banner-name@login': {
					templateUrl: '../partials/blog/banner.name.html',
					controller: function ($scope) {
						$scope.title = 'Login';
						$scope.subtitle = 'Please login to access restricted areas.';
					}
				},
				'banner-breadcrumbs@login': {
					templateUrl: '../partials/blog/banner.breadcrumbs.html',
					controller: function ($scope) {
						$scope.breadcrumbs = [
							{name: 'Home', sref: 'home'},
							{name: 'Login'}
						];
					}
				}
			}
		})

		.state('logout', {
			"url": '/logout',
			templateUrl: '../partials/logout.html',
			controller: 'LogoutCtr',
			access: {restricted: true}
		})

		.state('register', {
			"url": '/register',
			templateUrl: '../partials/register.html',
			controller: 'RegisterCtr',
			access: {restricted: false}
		})
});

app.run(function ($rootScope, $location, $state, AuthService) {
	$rootScope.$on('$stateChangeStart', function (event, next, current) {
		if (next.access.restricted && AuthService.isLoggedIn() === false) {
			event.preventDefault(); // stop current execution
			$state.go('login');
		}
	});
});