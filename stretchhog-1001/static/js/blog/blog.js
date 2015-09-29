var blogApp = angular.module('blogApp', ['ngResource', 'ngSanitize', 'ui.router']);

blogApp.config(['$interpolateProvider', function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{[');
	$interpolateProvider.endSymbol(']}')
}]);

