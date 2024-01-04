import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
x = 10
y = 20
print("Sum:", x + y)