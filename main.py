import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)