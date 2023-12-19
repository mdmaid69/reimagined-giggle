import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue