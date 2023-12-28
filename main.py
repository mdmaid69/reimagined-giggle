  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])