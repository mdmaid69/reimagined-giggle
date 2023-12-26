  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True