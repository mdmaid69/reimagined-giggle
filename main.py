  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
n = 10
print("Square numbers:", [x**2 for x in range(n)])