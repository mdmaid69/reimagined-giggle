  import os
  def get_current_directory():
        return os.getcwd()
def calculate_roi(gain, cost):
        return (gain - cost) / cost