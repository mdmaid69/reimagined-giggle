  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time