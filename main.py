def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))