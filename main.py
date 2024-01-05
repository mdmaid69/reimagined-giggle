n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)