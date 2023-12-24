  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def calculate_roi(gain, cost):
        return (gain - cost) / cost