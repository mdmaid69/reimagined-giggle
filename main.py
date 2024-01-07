import collections
def count_elements(iterable):
        return collections.Counter(iterable)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))