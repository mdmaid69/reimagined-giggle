  import os
  def get_base_name(path):
        return os.path.basename(path)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)