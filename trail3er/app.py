# -*- coding: utf-8 -*-

from flask import Flask, render_template
from .config import DefaultConfig


from .frontend import frontend
from .user import user # User
from .trailer import trailer

from .extensions import db
#from .utils import INSTANCE_FOLDER_PATH


# For import *
__all__ = ['create_app']

DEFAULT_BLUEPRINTS = (
    frontend, trailer, user,
)

def create_app(config=None, app_name=None, blueprints=None):
    """Create a Flask app."""

    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS


    app = Flask(app_name)
    configure_app(app, config)
    #configure_hook(app)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_template_filters(app)
    configure_error_handlers(app)

    return app


def configure_app(app, config=None):
    app.config.from_object(DefaultConfig)
    if config:
        app.config.from_object(config)

def configure_extensions(app):
    # flask-sqlalchemy
    db.init_app(app)
    
    # other extensions goes here



def configure_blueprints(app, blueprints):
    """Configure blueprints in views."""

    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_template_filters(app):

    @app.template_filter()
    def pretty_date(value):
        return pretty_date(value)

    @app.template_filter()
    def format_date(value, date_format='%Y-%m-%d'):
        return value.strftime(date_format)


def configure_hook(app):

    @app.before_request
    def before_request():
        pass


def configure_error_handlers(app):

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("errors/403.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/500.html"), 500
