  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)