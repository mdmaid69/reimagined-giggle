def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))