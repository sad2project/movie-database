#!python
from flask import Flask
from routes import routes

app = Flask(__name__)


def run():
    routes.register_routes(app)
    app.run(port=5000, debug=True)


if __name__ == "__main__":
    run()
