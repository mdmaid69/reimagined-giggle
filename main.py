print([x**2 for x in range(10)])
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)