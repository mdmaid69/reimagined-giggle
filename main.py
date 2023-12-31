  import os
  def get_current_working_directory():
        return os.getcwd()
n = 10
print("Square numbers:", [x**2 for x in range(n)])