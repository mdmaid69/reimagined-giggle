  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time