text = "Hello, world!"
print("Characters:", len(text))
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)