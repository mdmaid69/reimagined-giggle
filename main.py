import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a