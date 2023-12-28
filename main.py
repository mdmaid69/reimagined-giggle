def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))