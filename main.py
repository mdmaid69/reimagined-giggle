import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"