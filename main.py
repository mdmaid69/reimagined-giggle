  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
i = 0
while i < 5:
        print(i)
        i += 1