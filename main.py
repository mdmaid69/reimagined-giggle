  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  def cube_number(x):
        return x**3