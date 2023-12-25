import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def greet(name):
        print(f"Hello, {name}!")