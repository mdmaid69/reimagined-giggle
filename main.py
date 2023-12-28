def reverse_list(lst):
        return lst[::-1]
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())