import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets