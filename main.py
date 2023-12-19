n = 10
print("Square numbers:", [x**2 for x in range(n)])
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a