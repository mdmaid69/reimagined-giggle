  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps