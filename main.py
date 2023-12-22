n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)