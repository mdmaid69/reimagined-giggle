  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])