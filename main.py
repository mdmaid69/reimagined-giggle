import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import sklearn.datasets
print(sklearn.datasets.load_iris())