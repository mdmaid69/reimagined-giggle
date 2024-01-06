import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
def find_common_elements(list1, list2):
        return set(list1) & set(list2)