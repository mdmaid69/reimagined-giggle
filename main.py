import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list