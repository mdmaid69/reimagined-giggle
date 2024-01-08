  def calculate_circumference_circle(r):
        return 2 * 3.14 * r
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)