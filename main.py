  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a