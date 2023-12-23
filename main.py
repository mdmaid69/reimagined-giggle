import random
def generate_random_number(start, end):
        return random.randint(start, end)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a