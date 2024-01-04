  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])