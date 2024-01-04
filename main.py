def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))