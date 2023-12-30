import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import sklearn.datasets
print(sklearn.datasets.load_iris())