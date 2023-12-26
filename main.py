  import os
  def delete_file(file_name):
        os.remove(file_name)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])