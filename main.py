import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))