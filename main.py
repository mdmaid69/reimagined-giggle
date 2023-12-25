numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a