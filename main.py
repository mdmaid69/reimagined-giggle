  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)