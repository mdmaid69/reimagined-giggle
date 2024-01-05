import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))