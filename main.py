def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)