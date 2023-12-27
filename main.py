import sklearn.datasets
print(sklearn.datasets.load_iris())
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))