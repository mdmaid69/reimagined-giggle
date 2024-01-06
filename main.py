import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
def find_difference(list1, list2):
        return set(list1) - set(list2)