import random
def roll_die():
        return random.randint(1, 6)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a