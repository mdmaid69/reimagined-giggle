  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])