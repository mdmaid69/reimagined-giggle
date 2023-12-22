n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)