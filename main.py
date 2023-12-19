list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list