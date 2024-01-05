import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])