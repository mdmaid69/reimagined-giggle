import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))