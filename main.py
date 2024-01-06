import sys
def add_to_python_path(path):
        sys.path.append(path)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))