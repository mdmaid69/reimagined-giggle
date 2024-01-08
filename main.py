import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))