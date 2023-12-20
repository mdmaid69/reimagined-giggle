import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def find_unique_words(sentence):
        return set(sentence.split())