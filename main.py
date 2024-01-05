import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import array
def get_array_item_count(array, item):
        return array.count(item)