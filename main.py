import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import array
def get_array_item_count(array, item):
        return array.count(item)