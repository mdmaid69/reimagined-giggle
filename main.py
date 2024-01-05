def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks