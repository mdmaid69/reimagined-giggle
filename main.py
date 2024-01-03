import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
text = "Hello, world!"
print("Reversed:", text[::-1])