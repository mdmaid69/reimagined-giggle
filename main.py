import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)