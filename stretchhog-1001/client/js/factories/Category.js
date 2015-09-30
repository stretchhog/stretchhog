app.factory('Category', function ($resource) {
	return $resource('/blog-api/category/:key',
		{
			key: '@key'
		},
		{
			'update': {method: 'PUT'}
		});
});
