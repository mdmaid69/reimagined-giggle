import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import array
def get_bytes_from_array(array):
        return array.tobytes()