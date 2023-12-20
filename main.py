import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)