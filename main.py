import random
def roll_die():
        return random.randint(1, 6)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a