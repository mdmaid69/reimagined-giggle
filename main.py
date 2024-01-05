import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])