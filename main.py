n = 10
print("Powers of 2:", [2**x for x in range(n)])
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)