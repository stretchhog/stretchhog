app.factory('Category', function ($resource) {
	return $resource('/blog-api/admin/category/:key',
		{
			key: '@key'
		},
		{
			'update': {method: 'PUT'}
		});
});
