  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
def calculate_roi(gain, cost):
        return (gain - cost) / cost