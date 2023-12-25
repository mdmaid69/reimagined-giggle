n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)