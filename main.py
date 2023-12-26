import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"