import sklearn.datasets
print(sklearn.datasets.load_iris())
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))