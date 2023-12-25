import tensorflow as tf
print(tf.__version__)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)