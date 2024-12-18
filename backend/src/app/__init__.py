import os
from flask import Flask
from app.routes.auth_routes import auth_bp
from app.routes.book_routes import book_bp
from app.routes.post_routes import post_bp
from app.routes.reply_routes import reply_bp
from app.routes.home_routes import home_bp
from . import database

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    app.config['DATABASE'] = 'database.db'
    database.init_app(app)
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    app.register_blueprint(home_bp, url_prefix='/api/v1/')
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(book_bp, url_prefix='/api/v1/book')
    app.register_blueprint(post_bp, url_prefix='/api/v1/post')
    app.register_blueprint(reply_bp, url_prefix='/api/v1/reply')
    
    return app