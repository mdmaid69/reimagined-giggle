  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
for i in range(5):
        print(i)