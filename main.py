import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))