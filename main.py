import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)