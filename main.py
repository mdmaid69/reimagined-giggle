def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a