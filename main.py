def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)