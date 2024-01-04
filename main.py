import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))