import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a