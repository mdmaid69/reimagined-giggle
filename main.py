import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import random
def generate_random_number(start, end):
        return random.randint(start, end)