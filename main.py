def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()