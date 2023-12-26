import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)