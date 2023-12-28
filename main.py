numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)