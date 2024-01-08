import random
def generate_random_choice(choices):
        return random.choice(choices)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a