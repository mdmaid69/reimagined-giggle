  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True