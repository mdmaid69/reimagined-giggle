n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)