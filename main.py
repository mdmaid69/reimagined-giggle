import os
def get_environment_variable(var):
        return os.getenv(var)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))