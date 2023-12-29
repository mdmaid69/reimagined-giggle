  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
def calculate_area(radius):
        return 3.14 * radius * radius