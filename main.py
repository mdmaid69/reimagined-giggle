  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])