import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
n = 10
print("Powers of 2:", [2**x for x in range(n)])