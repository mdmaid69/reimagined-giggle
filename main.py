import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"