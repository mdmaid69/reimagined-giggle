  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal