import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import sklearn.datasets
print(sklearn.datasets.load_iris())