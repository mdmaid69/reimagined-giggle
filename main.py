import sklearn.datasets
print(sklearn.datasets.load_iris())
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)