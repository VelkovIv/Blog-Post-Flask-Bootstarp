import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = 'mysecretkey'
##########################
#### DATABASE SET UP ####
##########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
app.app_context().push()
Migrate(app, db)

#########################
# LOGIN CONFIGURATIONS #
#########################
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

##########################


from blog_post.core.views import core
from blog_post.users.views import users
from blog_post.blog_post.views import blog_posts
from blog_post.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)
