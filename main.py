import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)