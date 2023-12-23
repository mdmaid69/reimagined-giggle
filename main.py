def find_unique_words(sentence):
        return set(sentence.split())
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))