import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
def count_words(sentence):
        return len(sentence.split())