import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])