import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets