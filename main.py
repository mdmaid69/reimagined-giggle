  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True