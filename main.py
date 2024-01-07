  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
def calculate_roi(gain, cost):
        return (gain - cost) / cost