import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a