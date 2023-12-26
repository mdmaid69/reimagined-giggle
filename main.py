import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue