  import os
  def get_base_name(path):
        return os.path.basename(path)
def calculate_roi(gain, cost):
        return (gain - cost) / cost