import sklearn.datasets
print(sklearn.datasets.load_iris())
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)