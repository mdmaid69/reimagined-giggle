  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
def calculate_perpetuity(payment, rate):
        return payment / rate