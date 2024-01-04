  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
n = 10
print("Square numbers:", [x**2 for x in range(n)])