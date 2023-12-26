  import os
  def delete_file(file_name):
        os.remove(file_name)
def calculate_average(lst):
        return sum(lst) / len(lst)