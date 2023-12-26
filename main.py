import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
n = 10
print("Powers of 2:", [2**x for x in range(n)])