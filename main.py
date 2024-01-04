  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)