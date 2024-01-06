def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)