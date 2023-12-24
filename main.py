import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])