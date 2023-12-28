  def sort_list(lst):
        return sorted(lst)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)