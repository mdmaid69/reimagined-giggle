sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)