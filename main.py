import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)