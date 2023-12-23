import collections
def create_counter():
        return collections.Counter()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))