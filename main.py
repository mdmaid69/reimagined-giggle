def find_difference(list1, list2):
        return set(list1) - set(list2)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())