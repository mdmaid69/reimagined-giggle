  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)