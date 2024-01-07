import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import json
def read_from_json(json_string):
        return json.loads(json_string)