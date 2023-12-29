  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import sklearn.datasets
print(sklearn.datasets.load_iris())