  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
def calculate_power(work, time):
        return work / time