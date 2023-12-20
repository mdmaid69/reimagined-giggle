import array
def get_string_from_array(array):
        return array.tobytes()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"