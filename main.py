sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)