n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))