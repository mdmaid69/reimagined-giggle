import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))