import tensorflow as tf
print(tf.__version__)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)