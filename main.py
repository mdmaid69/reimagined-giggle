  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True