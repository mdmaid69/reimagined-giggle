import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))