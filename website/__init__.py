__all__ = ["app", "database", "model", "routes", "view", "modules"]

### List of work left:
#	TODO		[Meta]		Write readme (and license?)
#	OPTIONAL	[Structure]	Break the big files into modules based on feature
#	OPTIONAL	[Feature]		Backup
#	OPTIONAL	[Feature]		Cache

from app import app

if __name__ == '__main__':
	import os
	HOST = os.environ.get('SERVER_HOST', 'localhost')
	try:
		PORT = int(os.environ.get('SERVER_PORT', '5555'))
	except ValueError:
		PORT = 5555
	app.run(HOST, PORT)