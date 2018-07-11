from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

#This creates the application object as an instance of class Flask
app = Flask(__name__)
#I don't know what config is. 
app.config.from_object(Config)
#This creates a database object (db). 
db = SQLAlchemy(app)
#This represents a migration engine. 
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login'

#Routes refers to the different URLs that the app will implement. 
#Models will define its structure. 
from app import routes, models