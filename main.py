import array
def get_array_as_memoryview(array):
        return memoryview(array)
import random
def roll_die():
        return random.randint(1, 6)