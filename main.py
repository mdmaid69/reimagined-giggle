x = 10
y = 20
print("Sum:", x + y)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a