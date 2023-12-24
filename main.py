  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def calculate_average(numbers):
        return sum(numbers) / len(numbers)