import sklearn.datasets
print(sklearn.datasets.load_iris())
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)