import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"