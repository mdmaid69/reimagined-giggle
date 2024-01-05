def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a