#!python
from flask import Flask
from routes import routes

app = Flask(__name__)


def run():
    app.register_blueprint(routes)
    app.run(port=5000, debug=True)


if __name__ == "__main__":
    run()
