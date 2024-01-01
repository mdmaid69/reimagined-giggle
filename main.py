  def convert_to_octal(n):
        return oct(n)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)