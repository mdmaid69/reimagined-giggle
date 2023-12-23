import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
n = 10
print("Square numbers:", [x**2 for x in range(n)])