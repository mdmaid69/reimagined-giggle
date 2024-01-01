  import os
  def get_directory_name(path):
        return os.path.dirname(path)
def calculate_roi(gain, cost):
        return (gain - cost) / cost