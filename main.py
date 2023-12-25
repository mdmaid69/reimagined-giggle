n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import collections
def count_elements(iterable):
        return collections.Counter(iterable)