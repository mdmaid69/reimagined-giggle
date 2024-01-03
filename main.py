n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
  import os
  def delete_file(file_name):
        os.remove(file_name)