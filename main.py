  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
def calculate_perpetuity(payment, rate):
        return payment / rate