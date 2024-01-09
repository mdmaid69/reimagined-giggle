def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]