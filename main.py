import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal