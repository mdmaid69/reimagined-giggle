n = 10
print("Powers of 2:", [2**x for x in range(n)])
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a