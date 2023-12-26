import random
print(random.randint(0, 100))
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)