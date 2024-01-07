  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])