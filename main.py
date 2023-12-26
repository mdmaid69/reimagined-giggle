def calculate_roi(gain, cost):
        return (gain - cost) / cost
  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime