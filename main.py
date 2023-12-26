  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
def is_even(n):
        return n % 2 == 0