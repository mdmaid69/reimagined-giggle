  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))