import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import os
def get_current_working_directory():
        return os.getcwd()