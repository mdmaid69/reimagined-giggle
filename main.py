import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))