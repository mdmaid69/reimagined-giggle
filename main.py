import array
def get_bytes_from_array(array):
        return array.tobytes()
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"