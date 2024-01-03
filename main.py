import random
print(random.randint(0, 100))
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)