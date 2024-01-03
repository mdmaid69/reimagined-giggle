import random
def generate_random_choice(choices):
        return random.choice(choices)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a