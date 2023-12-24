import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets