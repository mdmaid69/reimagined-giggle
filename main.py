n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)