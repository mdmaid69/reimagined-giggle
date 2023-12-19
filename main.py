import sklearn.datasets
print(sklearn.datasets.load_iris())
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h