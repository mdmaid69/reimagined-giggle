  import os
  def split_path(path):
        return os.path.split(path)
def calculate_roi(gain, cost):
        return (gain - cost) / cost