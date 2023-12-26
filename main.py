import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"