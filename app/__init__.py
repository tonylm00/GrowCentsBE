from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .Config import Config

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from .routes import blog_routes, mifid_routes, trade_routes, esg_routes
        from app.models import add_blog_articles

        app.register_blueprint(blog_routes.bp)
        app.register_blueprint(mifid_routes.bp)
        app.register_blueprint(trade_routes.bp)
        app.register_blueprint(esg_routes.bp)

        db.create_all()
        add_blog_articles()

    return app
