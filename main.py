text = "Hello, world!"
print("Reversed:", text[::-1])
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)