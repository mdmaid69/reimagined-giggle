  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])