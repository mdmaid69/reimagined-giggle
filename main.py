import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
n = 10
print("Cube numbers:", [x**3 for x in range(n)])