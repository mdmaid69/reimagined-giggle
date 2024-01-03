  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
def calculate_speed(distance, time):
        return distance / time