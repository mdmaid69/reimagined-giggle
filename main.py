import sklearn.datasets
print(sklearn.datasets.load_iris())
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)