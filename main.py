  import os
  def split_path(path):
        return os.path.split(path)
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True