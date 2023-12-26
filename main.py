import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])