app.factory('Entry', function ($resource) {
	return $resource('/blog-api/admin/entry/:key',
			{
				key: '@key'
			},
			{
				'update': {method: 'PUT'}
			});
}) ;
