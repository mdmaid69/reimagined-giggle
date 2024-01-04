  import os
  def get_current_directory():
        return os.getcwd()
n = 10
print("Cube numbers:", [x**3 for x in range(n)])