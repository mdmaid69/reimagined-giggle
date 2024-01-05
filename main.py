import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])