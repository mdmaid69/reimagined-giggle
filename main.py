  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])