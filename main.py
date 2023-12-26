  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True