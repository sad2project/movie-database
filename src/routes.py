from flask.blueprints import Blueprint

routes = Blueprint('main', __name__)


@routes.route('/')
def index():
    return "Welcome Home!"