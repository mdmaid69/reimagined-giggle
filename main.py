import array
def convert_array_to_bytes(array):
        return array.tobytes()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"