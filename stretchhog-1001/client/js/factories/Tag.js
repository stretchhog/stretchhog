app.factory('Tag', function ($resource) {
	return $resource('/blog-api/tag/:key',
		{
			key: '@key'
		},
		{
			'update': {method: 'PUT'}
		});
});

