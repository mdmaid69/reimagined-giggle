import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"