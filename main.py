import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import shutil
def delete_directory(path):
        shutil.rmtree(path)