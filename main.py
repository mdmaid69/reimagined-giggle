import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])