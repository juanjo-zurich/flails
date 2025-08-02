from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import config

# Initialize Flask extensions
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
migrate = Migrate()
def create_app(config_name='default'):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config[config_name])

    # Initialize extensions with app
    db.init_app(flask_app)
    login_manager.init_app(flask_app)
    migrate.init_app(flask_app, db)

    # Register blueprints
    from app.auth import bp as auth_bp
    flask_app.register_blueprint(auth_bp, url_prefix='/auth')

    # Initialize admin
    from flask_admin import Admin
    flask_admin = Admin(name='test_project Admin', template_mode='bootstrap4')
    import app.admin
    flask_admin.init_app(flask_app)
    app.admin.init_admin(flask_app, flask_admin)

    return flask_app