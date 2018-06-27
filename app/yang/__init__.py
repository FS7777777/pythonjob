import os
from flask import Flask
from flask_cors import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
# sqlite:/// 三个标示相对路径 四个标示绝对路径
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#声明db
db = SQLAlchemy(app)

def Create_app(test_config=None):

    # 跨域设置
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

    from yang import auth,blog,exception
    app.register_blueprint(auth.api)
    app.register_blueprint(blog.api)
    app.register_blueprint(exception.exception)
    return app


# if __name__=='__main__':
#     Create_app().run()