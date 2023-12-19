import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
i = 0
while i < 5:
        print(i)
        i += 1