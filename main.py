def find_unique_words(sentence):
        return set(sentence.split())
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)