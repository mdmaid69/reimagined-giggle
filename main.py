import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
text = "Hello, world!"
print("Reversed:", text[::-1])