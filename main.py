from collections import Counter
print(Counter("hello world"))
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)