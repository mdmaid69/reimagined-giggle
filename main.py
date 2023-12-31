import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b