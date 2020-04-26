from hypothesis import given, settings, assume, strategies as strat


def properties(**kwargs):
    return lambda func: given(**kwargs)(settings(max_examples=10)(func))