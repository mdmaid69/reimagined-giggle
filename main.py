  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))