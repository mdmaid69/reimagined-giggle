import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)