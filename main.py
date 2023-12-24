  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def calculate_perpetuity(payment, rate):
        return payment / rate