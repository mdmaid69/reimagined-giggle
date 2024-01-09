import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])