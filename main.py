  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def calculate_volume(length, width, height):
        return length * width * height