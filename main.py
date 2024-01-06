import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding