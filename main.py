import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"