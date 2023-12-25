import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)