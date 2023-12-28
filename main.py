  def is_odd(n):
        return n % 2 != 0
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)