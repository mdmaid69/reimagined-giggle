  import os
  def get_base_name(path):
        return os.path.basename(path)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal