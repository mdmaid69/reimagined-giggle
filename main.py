text = "Hello, world!"
print("Words:", len(text.split()))
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)