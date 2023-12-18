import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))