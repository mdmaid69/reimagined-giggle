n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)