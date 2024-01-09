import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)