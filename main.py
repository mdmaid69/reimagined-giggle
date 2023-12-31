import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def count_words(sentence):
        return len(sentence.split())