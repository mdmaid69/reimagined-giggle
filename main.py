import tensorflow as tf
print(tf.__version__)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)