n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import collections
def count_elements(iterable):
        return collections.Counter(iterable)