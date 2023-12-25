import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets