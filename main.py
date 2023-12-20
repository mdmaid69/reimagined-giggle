  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
n = 10
print("Square numbers:", [x**2 for x in range(n)])