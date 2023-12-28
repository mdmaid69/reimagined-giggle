def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))