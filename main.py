import random
print(random.randint(0, 100))
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)