import sklearn.datasets
print(sklearn.datasets.load_iris())
import json
def read_from_json(json_string):
        return json.loads(json_string)