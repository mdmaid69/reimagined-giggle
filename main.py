import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list