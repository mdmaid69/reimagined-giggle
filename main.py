n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks