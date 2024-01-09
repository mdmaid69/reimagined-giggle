import tensorflow as tf
print(tf.__version__)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)