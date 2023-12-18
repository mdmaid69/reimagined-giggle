import itertools
print(list(itertools.permutations([1, 2, 3])))
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))