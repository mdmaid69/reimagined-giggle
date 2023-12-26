  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True