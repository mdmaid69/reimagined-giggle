import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])