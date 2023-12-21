import tensorflow as tf
print(tf.__version__)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)