import sklearn.datasets
print(sklearn.datasets.load_iris())
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))