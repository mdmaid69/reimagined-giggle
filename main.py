n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import collections
def count_elements(iterable):
        return collections.Counter(iterable)