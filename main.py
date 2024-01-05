def calculate_roi(gain, cost):
        return (gain - cost) / cost
  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid