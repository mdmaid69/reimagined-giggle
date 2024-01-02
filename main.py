import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))