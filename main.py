from collections import Counter
print(Counter("hello world"))
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)