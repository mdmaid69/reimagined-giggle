text = "Hello, world!"
print("Reversed:", text[::-1])
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a