import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"