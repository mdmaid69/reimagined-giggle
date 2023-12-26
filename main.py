  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True