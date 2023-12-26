n = 10
print("Powers of 2:", [2**x for x in range(n)])
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a