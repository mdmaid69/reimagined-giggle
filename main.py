text = "Hello, world!"
print("Characters:", len(text))
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a