import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)