text = "Hello, world!"
print("Words:", len(text.split()))
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)