import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])