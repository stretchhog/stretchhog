app.factory('Entry', function ($resource) {
	return $resource('/blog-api/entry/:key',
			{
				key: '@key'
			},
			{
				'update': {method: 'PUT'}
			});
}) ;
