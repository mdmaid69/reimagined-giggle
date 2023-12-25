n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a