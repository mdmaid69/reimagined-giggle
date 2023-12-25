def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)