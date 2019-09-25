from router import Router

import pytest


def test_starts_with_empty_routes():
    router = Router()
    assert len(router.routes) == 0


def test_adds_first_route():
    router = Router()

    @router.route("route")
    def routed_func(): pass

    assert len(router.routes) == 1
    assert router.routes[0][0] == "route"
    assert router.routes[0][1] == routed_func


def test_adds_more_routes():
    router = Router()

    @router.route("route1")
    def func1(): pass

    @router.route("route2")
    def func2(): pass

    assert len(router.routes) == 2
    assert router.routes[1][0] == "route2"
    assert router.routes[1][1] == func2
