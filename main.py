import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue