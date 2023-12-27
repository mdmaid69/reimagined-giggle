def remove_duplicates(lst):
        return list(set(lst))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())