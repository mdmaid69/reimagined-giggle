import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
text = "Hello, world!"
print("Reversed:", text[::-1])