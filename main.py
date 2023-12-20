print([x**2 for x in range(10)])
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)