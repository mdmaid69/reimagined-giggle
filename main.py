import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import sklearn.datasets
print(sklearn.datasets.load_iris())