import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding