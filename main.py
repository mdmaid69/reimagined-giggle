import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)