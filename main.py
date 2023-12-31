  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
def calculate_perpetuity(payment, rate):
        return payment / rate