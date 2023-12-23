import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)