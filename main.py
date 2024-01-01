import sklearn.datasets
print(sklearn.datasets.load_iris())
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)