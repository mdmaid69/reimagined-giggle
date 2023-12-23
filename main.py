n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)