import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def greet(name):
        print(f"Hello, {name}!")