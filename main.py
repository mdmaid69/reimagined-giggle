import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list