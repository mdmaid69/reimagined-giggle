for i in range(10): print(i)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)