import sklearn.datasets
print(sklearn.datasets.load_iris())
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)