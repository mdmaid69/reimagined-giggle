  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
n = 10
print("Cube numbers:", [x**3 for x in range(n)])