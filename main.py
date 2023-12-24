def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))