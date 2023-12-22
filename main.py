  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
def calculate_volume(length, width, height):
        return length * width * height