  import sys
  def get_python_version():
        return sys.version
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)