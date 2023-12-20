import numpy as np
print(np.array([1, 2, 3]))
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))