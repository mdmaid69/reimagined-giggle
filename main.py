n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)