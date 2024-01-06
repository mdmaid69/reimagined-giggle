import itertools
print(list(itertools.permutations([1, 2, 3])))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())