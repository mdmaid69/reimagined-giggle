import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import os
def get_file_size(filename):
        return os.path.getsize(filename)