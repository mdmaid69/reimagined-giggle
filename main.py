def calculate_roi(gain, cost):
        return (gain - cost) / cost
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)