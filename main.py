import os
def get_current_working_directory():
        return os.getcwd()
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True