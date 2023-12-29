import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))