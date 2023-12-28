import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets