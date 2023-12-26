import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)