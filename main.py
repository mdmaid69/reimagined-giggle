import json
def convert_to_json(data):
        return json.dumps(data)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))