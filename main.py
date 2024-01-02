import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  def calculate_area_circle(r):
        return 3.14 * r**2