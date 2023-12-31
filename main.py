import collections
def create_user_string():
        return collections.UserString()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())