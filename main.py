import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))