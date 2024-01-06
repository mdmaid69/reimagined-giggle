import random
print(random.randint(0, 100))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)