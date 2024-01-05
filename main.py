import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
text = "Hello, world!"
print("Characters:", len(text))