  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time