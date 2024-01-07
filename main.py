import platform
def get_python_version():
        return platform.python_version()
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"