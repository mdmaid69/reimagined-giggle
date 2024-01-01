import collections
def create_priority_queue():
        return collections.deque()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())