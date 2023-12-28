import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)