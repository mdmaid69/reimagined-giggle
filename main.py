n = 10
print("Square numbers:", [x**2 for x in range(n)])
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)