import array
def get_array_buffer_info(array):
        return array.buffer_info()
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"