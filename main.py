  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
text = "Hello, world!"
print("Words:", len(text.split()))