import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"