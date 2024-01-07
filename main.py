import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities