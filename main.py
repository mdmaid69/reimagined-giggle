n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import collections
def count_elements(iterable):
        return collections.Counter(iterable)