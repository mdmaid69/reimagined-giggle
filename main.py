import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import tensorflow as tf
print(tf.__version__)