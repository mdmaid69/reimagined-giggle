import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])