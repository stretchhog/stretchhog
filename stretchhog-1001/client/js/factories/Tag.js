app.factory('Tag', function ($resource) {
	return $resource('/blog-api/admin/tag/:key',
		{
			key: '@key'
		},
		{
			'update': {method: 'PUT'}
		});
});

