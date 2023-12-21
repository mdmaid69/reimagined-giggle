import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))