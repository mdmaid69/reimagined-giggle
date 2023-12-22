def calculate_roi(gain, cost):
        return (gain - cost) / cost
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]