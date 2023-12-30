import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b