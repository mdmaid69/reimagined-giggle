import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time