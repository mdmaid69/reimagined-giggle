import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))