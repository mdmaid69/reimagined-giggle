n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))