import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list