  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)