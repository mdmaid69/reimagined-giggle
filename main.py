def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)