numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a