  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True