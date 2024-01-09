import sklearn.datasets
print(sklearn.datasets.load_iris())
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)