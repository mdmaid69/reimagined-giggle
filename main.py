def calculate_roi(gain, cost):
        return (gain - cost) / cost
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)