  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True