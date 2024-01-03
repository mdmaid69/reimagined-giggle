n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a