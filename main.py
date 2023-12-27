  import os
  def delete_file(file_name):
        os.remove(file_name)
def calculate_roi(gain, cost):
        return (gain - cost) / cost