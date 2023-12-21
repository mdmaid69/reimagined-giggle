import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])