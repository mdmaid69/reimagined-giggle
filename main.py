import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height