import sklearn.datasets
print(sklearn.datasets.load_iris())
import json
def convert_to_json(data):
        return json.dumps(data)