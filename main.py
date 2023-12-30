def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)