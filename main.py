n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]