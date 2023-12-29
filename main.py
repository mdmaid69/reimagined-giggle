import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import itertools
print(list(itertools.permutations([1, 2, 3])))