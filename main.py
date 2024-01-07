def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import os
  def delete_file(file_name):
        os.remove(file_name)