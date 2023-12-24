sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))