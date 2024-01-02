import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))