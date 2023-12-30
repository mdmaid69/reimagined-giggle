import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets