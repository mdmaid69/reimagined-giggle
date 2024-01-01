import tensorflow as tf
print(tf.__version__)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h