  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
def calculate_roi(gain, cost):
        return (gain - cost) / cost