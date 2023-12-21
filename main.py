import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h