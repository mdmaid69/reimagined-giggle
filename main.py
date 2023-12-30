  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time