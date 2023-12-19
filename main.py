  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
def calculate_roi(gain, cost):
        return (gain - cost) / cost