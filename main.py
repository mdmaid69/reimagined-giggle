import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"