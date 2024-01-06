import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)