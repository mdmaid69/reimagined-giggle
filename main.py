import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities