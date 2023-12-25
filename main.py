import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"