sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))