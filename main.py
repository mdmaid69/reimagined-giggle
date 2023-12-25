import sklearn.datasets
print(sklearn.datasets.load_iris())
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)