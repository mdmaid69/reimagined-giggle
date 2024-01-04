def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)