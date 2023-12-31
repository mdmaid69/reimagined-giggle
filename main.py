import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue