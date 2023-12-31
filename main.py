import collections
def create_queue():
        return collections.deque()
def find_unique_words(sentence):
        return set(sentence.split())