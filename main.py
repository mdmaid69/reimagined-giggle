import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding