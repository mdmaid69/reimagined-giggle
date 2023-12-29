import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets