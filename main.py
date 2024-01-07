import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)