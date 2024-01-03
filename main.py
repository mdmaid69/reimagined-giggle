  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])