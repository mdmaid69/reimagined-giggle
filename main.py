import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import os
def remove_directory(path):
        os.rmdir(path)