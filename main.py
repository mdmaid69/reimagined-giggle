  import os
  def get_current_directory():
        return os.getcwd()
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))