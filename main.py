  import sys
  def get_python_version():
        return sys.version
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)