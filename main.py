import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)