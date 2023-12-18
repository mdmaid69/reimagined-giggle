import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])