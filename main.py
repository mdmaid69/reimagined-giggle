import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import sklearn.datasets
print(sklearn.datasets.load_iris())