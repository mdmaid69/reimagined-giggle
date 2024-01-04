def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)