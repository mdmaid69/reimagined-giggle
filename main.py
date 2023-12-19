text = "Hello, world!"
print("Words:", len(text.split()))
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))