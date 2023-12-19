import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b