n = 10
print("Square numbers:", [x**2 for x in range(n)])
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)