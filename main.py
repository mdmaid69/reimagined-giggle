def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))