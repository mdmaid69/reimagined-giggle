import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import sklearn.datasets
print(sklearn.datasets.load_iris())