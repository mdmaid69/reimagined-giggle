  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True