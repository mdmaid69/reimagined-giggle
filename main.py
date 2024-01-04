import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import random
def generate_random_number(start, end):
        return random.randint(start, end)