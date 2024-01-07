import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b