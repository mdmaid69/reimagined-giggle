  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
def calculate_volume(length, width, height):
        return length * width * height