import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list