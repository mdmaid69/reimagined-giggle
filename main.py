  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)