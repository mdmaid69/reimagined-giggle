  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))