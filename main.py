import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
n = 10
print("Square numbers:", [x**2 for x in range(n)])