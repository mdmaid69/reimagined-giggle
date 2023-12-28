  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
def calculate_roi(gain, cost):
        return (gain - cost) / cost