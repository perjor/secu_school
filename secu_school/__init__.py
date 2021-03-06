from flask import Flask, request
from .extensions import mysql, csrf, toolbar

def create_app():
    app = Flask(__name__, instance_relative_config=True) # , instance_relative_config=True

    app.config.from_object('config.default')
    app.config.from_pyfile('config.py', silent=True)
    app.config.from_object('config.production')

    # import secu_school.views
    from .views.home import home
    from .views.dashboard import dashboard
    from .views.klas import klas
    from .views.richting import richting
    from .views.leraar import leraar

    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    app.register_blueprint(klas)
    app.register_blueprint(richting)
    app.register_blueprint(leraar)


    # init MySQL
    mysql.init_app(app)
    csrf.init_app(app)
    toolbar.init_app(app)

    return app
