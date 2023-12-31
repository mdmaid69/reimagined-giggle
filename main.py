sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))