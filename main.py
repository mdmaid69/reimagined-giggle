import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities