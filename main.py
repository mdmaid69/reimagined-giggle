text = "Hello, world!"
print("Characters:", len(text))
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)