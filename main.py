  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
def calculate_roi(gain, cost):
        return (gain - cost) / cost