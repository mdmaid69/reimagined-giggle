  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])