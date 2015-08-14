from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.config.from_pyfile("config.py")

login_manager = LoginManager(app)


# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


#Include all routes
from routes import *


if __name__ == '__main__':
	import os
	HOST = os.environ.get('SERVER_HOST', 'localhost')
	try:
		PORT = int(os.environ.get('SERVER_PORT', '5555'))
	except ValueError:
		PORT = 5555
	app.run(HOST, PORT)

	
import database
if not database.check_if_setup():
	if app.config['DATABASE_SCHEMA_ERROR_ACTION'] == 'NOTHING':
		print("The Database Schema doesn't match the website, check the database or use the 'Reset Database' function (in /admin/setup/) to remove old data")
		flash("The Database Schema doesn't match the website, check the database or use the 'Reset Database' function (in <a href='/admin/setup/'>/admin/setup/</a>)to remove old data", "danger")
	else:
		database.reset_db()
		print("The Database has been reset due to not matching the website")
		flash("The Database has been reset due to not matching the website", "danger")