  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])