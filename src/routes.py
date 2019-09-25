from router import Router

routes = Router()


@routes.route('/')
def index():
    return "Welcome Home!"