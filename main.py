  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
text = "Hello, world!"
print("Words:", len(text.split()))