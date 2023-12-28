import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))