import os
from flask import Flask
from flask_cors import *

def Create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app,supports_credentials=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from yang import auth,blog
    app.register_blueprint(auth.api)
    app.register_blueprint(blog.api)

    return app


# if __name__=='__main__':
#     Create_app().run()