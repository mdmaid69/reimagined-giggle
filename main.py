n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)