import tensorflow as tf
print(tf.__version__)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)