import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
text = "Hello, world!"
print("Words:", len(text.split()))