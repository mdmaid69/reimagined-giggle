from collections import Counter
print(Counter("hello world"))
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)