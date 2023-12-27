import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import sklearn.datasets
print(sklearn.datasets.load_iris())