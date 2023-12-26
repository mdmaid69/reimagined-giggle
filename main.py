import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
text = "Hello, world!"
print("Reversed:", text[::-1])