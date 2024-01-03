text = "Hello, world!"
print("Words:", len(text.split()))
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]