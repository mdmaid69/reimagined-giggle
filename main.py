  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
n = 10
print("Powers of 2:", [2**x for x in range(n)])