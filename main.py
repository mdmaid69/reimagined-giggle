  import os
  def get_base_name(path):
        return os.path.basename(path)
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True