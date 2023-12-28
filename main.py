import os
def change_working_directory(path):
        os.chdir(path)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))