import sklearn.datasets
print(sklearn.datasets.load_iris())
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)