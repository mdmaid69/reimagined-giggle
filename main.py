  import os
  def delete_file(file_name):
        os.remove(file_name)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])