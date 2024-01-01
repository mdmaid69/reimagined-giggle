import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import random
def roll_die():
        return random.randint(1, 6)