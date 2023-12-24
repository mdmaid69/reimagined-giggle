  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time