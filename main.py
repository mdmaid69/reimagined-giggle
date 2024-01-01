import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))