import tensorflow as tf
print(tf.__version__)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)