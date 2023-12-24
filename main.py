def greet(name):
        print(f"Hello, {name}!")
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a