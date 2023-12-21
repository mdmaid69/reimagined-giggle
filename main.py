import collections
def create_queue():
        return collections.deque()
def count_words(sentence):
        return len(sentence.split())