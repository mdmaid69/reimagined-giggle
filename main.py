import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)