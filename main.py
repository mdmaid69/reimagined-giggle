  def calculate_area_triangle(b, h):
        return 0.5 * b * h
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)