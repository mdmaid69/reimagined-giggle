def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list