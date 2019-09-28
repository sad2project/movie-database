class Router:
    def __init__(self):
        self.routes = []

    def route(self, path):
        def decorator(func):
            self.routes.append((path, func))
            return func
        return decorator

    def register_routes(self, router):
        for route in self.routes:
            router.route(route[0])(route[1])

    def register_subroutes(self, super_route, router):
        for route in self.routes:
            router.route(super_route + route[0])(route[1])
