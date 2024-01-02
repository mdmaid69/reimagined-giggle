n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)