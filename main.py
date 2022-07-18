from flask import Flask
from routes.index import main

def register_blueprints(app: Flask) -> None:
    app.register_blueprint(main)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    register_blueprints(app=app)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)