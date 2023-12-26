  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def calculate_perpetuity(payment, rate):
        return payment / rate