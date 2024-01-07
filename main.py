  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))