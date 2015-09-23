var blogApp = angular.module('blogApp', ['ngResource']);

blogApp.config(['$interpolateProvider', function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{[');
	$interpolateProvider.endSymbol(']}')
}]);