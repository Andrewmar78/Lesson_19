from flask import Flask
from flask_restx import Api

from app.config import Config
from app.dao.models.user import User
from app.setup_db import db
from app.views.auth import auth_ns
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.user import user_ns


def create_app(config: Config) -> Flask:
    """Функция создания основного объекта app"""
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    # configure_app(app)
    return application


def configure_app(application: Flask):
    """Функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)"""
    db.init_app(application)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    # create_data(app, db)


# def create_data():
#     """Создание пользователей в БД"""
#     with app.app_context():
#         db.create_all()
#
#         u1 = User(username="Vasya", password="my_little_pony", role="user")
#         u2 = User(username="Oleg", password="qwerty", role="user")
#         u3 = User(username="Oleg", password="P@ssw0rd", role="admin")
#
#         with db.session.begin():
#             db.session.add_all([u1, u2, u3])


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    # create_data()
    app.run(host="localhost", port=10001)
