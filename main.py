  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
def calculate_power(work, time):
        return work / time