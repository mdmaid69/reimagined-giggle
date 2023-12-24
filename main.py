numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list