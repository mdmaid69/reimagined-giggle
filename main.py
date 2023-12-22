  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
text = "Hello, world!"
print("Words:", len(text.split()))