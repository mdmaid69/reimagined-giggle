  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
for i in range(10): print(i)