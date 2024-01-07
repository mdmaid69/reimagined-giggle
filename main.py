  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])