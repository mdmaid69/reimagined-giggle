import collections
def create_user_list():
        return collections.UserList()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())