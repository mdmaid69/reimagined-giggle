import array
def get_array_as_frozenset(array):
        return frozenset(array)
import sklearn.datasets
print(sklearn.datasets.load_iris())