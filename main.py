import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  def calculate_area_rectangle(l, w):
        return l * w