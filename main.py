import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"