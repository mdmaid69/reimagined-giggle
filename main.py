  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])