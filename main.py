def count_characters(sentence):
        return len(sentence)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))