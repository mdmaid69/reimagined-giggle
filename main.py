numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a