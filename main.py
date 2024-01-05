n = 10
print("Cube numbers:", [x**3 for x in range(n)])
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)