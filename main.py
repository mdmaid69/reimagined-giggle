import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a