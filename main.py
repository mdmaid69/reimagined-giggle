import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))