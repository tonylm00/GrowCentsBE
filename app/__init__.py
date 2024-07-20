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
        from .routes import todo_routes, blog_routes, mifid_routes, trade_routes
        from app.populate_db.populate_blog import init_db_data

        app.register_blueprint(todo_routes.bp)
        app.register_blueprint(blog_routes.bp)
        app.register_blueprint(mifid_routes.bp)
        app.register_blueprint(trade_routes.bp)

        db.create_all()
        init_db_data()

    return app
