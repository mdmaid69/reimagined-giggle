import collections
def create_ordered_dict():
        return collections.OrderedDict()
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b