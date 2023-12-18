  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)