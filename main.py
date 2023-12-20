  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
def calculate_average(lst):
        return sum(lst) / len(lst)