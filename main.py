import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
n = 10
print("Cube numbers:", [x**3 for x in range(n)])