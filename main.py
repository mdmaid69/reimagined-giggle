import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity