  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  def square_number(x):
        return x**2